from fastapi import HTTPException
from services.servicesEncry import encrypt_message_aes, decrypt_message_aes,encrypt_message_3ds,decrypt_message_3ds,encrypt_message_RC4,decrypt_message_RC4
from services.servicesEncry import encrypt_message_Chacha20,decrypt_message_Chacha20,generate_rsa_keys,rsa_key_to_base64,rsa_base64_to_private_key,rsa_base64_to_public_key,rsa_encrypt_message,rsa_decrypt_message

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

    
#******************************************************RC4***************************************************************
    
def generate_key_RC4() -> str:
    """Génère une clé 3des encodée en base64."""
    key = os.urandom(16)
    return base64.b64encode(key).decode('utf-8')

def handle_encrypt_RC4(request: EncryptRequest) -> str:
    """Traite la requête de chiffrement 3DES."""
    try:
        return encrypt_message_RC4(request.message, request.key)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur lors du chiffrement : {str(e)}")
    
def handle_decrypt_RC4(request: DecryptRequest) -> str:
    """Traite la requête de déchiffrement 3DES."""
    try:
        return decrypt_message_RC4(request.encrypted_message, request.key)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur lors du déchiffrement : {str(e)}")
    
    
    
#******************************************************CHACHA20***************************************************************

def generate_key_Chacha20() -> str:
    """Génère une clé 3des encodée en base64."""
    key = os.urandom(32)
    return base64.b64encode(key).decode('utf-8')

def handle_encrypt_Chacha20(request: EncryptRequest) -> str:
    """Traite la requête de chiffrement chacha20."""
    try:
        return encrypt_message_Chacha20(request.message, request.key)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur lors du chiffrement : {str(e)}")
    
def handle_decrypt_Chacha20(request: DecryptRequest) -> str:
    """Traite la requête de déchiffrement chacha20."""
    try:
        return decrypt_message_Chacha20(request.encrypted_message, request.key)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur lors du déchiffrement : {str(e)}")
    
    

#******************************************************RSA***************************************************************



def handle_generate_keys()->str:
    """Génère des clés RSA et retourne leur représentation Base64."""
    try:
        private_key, public_key = generate_rsa_keys()
        private_key_b64 = rsa_key_to_base64(private_key, is_private=True)
        public_key_b64 = rsa_key_to_base64(public_key)
        return {"private_key": private_key_b64, "public_key": public_key_b64}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la génération des clés : {str(e)}")

def handle_encrypt_message(request: EncryptRequest)->str:
    """Traite une requête de chiffrement RSA."""
    try:
        public_key = rsa_base64_to_public_key(request.key)#public key
        ciphertext = rsa_encrypt_message(request.message.encode(), public_key)
        return {"ciphertext": ciphertext.hex()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur lors du chiffrement : {str(e)}")

def handle_decrypt_message(request: DecryptRequest)->str:
    """Traite une requête de déchiffrement RSA."""
    try:
        ciphertext = bytes.fromhex(request.encrypted_message)
        private_key = rsa_base64_to_private_key(request.key)#private key
        plaintext = rsa_decrypt_message(ciphertext, private_key)
        return {"plaintext": plaintext.decode()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur lors du déchiffrement : {str(e)}")

