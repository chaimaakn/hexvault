from fastapi import HTTPException
from services.servicesEncry import encrypt_message_aes, decrypt_message_aes,encrypt_message_3ds,decrypt_message_3ds
from models.encry import EncryptRequest, DecryptRequest
import os
import base64

#******************************************************AES***************************************************************
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
    
    
#******************************************************3DES***************************************************************
    
def generate_key_3des() -> str:
    """Génère une clé 3des encodée en base64."""
    key = os.urandom(24)
    return base64.b64encode(key).decode('utf-8')


def handle_encrypt_3des(request: EncryptRequest) -> str:
    """Traite la requête de chiffrement 3DES."""
    try:
        return encrypt_message_3ds(request.message, request.key)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur lors du chiffrement : {str(e)}")
    
def handle_decrypt_3des(request: DecryptRequest) -> str:
    """Traite la requête de déchiffrement 3DES."""
    try:
        return decrypt_message_3ds(request.encrypted_message, request.key)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur lors du déchiffrement : {str(e)}")
