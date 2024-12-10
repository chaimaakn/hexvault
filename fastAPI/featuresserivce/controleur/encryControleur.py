from fastapi import HTTPException
from services.servicesEncry import encrypt_message_aes, decrypt_message_aes
from models.encry import EncryptRequest, DecryptRequest
import os
import base64

def generate_key_aes() -> str:
    """Génère une clé AES encodée en base64."""
    key = os.urandom(32)
    return base64.b64encode(key).decode('utf-8')

def handle_encrypt_aes(request: EncryptRequest) -> str:
    """Traite la requête de chiffrement AES."""
    try:
        return encrypt_message_aes(request.message, request.key)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur lors du chiffrement : {str(e)}")

def handle_decrypt_aes(request: DecryptRequest) -> str:
    """Traite la requête de déchiffrement AES."""
    try:
        return decrypt_message_aes(request.encrypted_message, request.key)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur lors du déchiffrement : {str(e)}")
