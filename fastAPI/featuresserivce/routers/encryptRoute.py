from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
import base64

# Création du router
router = APIRouter()

# Utilitaires de chiffrement/déchiffrement
def pad_messageaes(message: bytes) -> bytes:
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    return padder.update(message) + padder.finalize()

def unpad_messageaes(padded_message: bytes) -> bytes:
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    return unpadder.update(padded_message) + unpadder.finalize()

def encrypt_messageaes(message: str, encoded_key: str) -> str:
    iv = os.urandom(16)
    key = base64.b64decode(encoded_key)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_message = pad_messageaes(message.encode('utf-8'))
    ciphertext = encryptor.update(padded_message) + encryptor.finalize()
    return base64.b64encode(iv + ciphertext).decode('utf-8')

def decrypt_messageaes(encoded_ciphertext: str, encoded_key: str) -> str:
    ciphertext = base64.b64decode(encoded_ciphertext)
    key = base64.b64decode(encoded_key)
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_message = decryptor.update(actual_ciphertext) + decryptor.finalize()
    return unpad_messageaes(padded_message).decode('utf-8')

# Modèles de données pour les requêtes
class EncryptRequest(BaseModel):
    message: str
    key: str

class DecryptRequest(BaseModel):
    encrypted_message: str
    key: str

# Routes du router
@router.get("/generate-key/AES", response_model=str)
async def generate_key():

    key = os.urandom(32)
    return base64.b64encode(key).decode('utf-8')

@router.post("/encrypt/AES", response_model=str)
async def encrypt(request: EncryptRequest):

    try:
        encrypted_message = encrypt_messageaes(request.message, request.key)
        return encrypted_message
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur lors du chiffrement : {str(e)}")

@router.post("/decrypt/AES", response_model=str)
async def decrypt(request: DecryptRequest):

    try:
        decrypted_message = decrypt_messageaes(request.encrypted_message, request.key)
        return decrypted_message
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur lors du déchiffrement : {str(e)}")
