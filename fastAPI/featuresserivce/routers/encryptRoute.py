from fastapi import APIRouter
from controleur.encryControleur import generate_key_aes, handle_encrypt_aes, handle_decrypt_aes,generate_key_3des,handle_decrypt_3des,handle_encrypt_3des
from models.encry import EncryptRequest, DecryptRequest

router = APIRouter()


#********************************AES*************************************************


@router.get("/generate-key/AES", response_model=str)
async def generate_key():
    """Route pour générer une clé AES."""
    return generate_key_aes()

@router.post("/encrypt/AES", response_model=str)
async def encrypt(request: EncryptRequest):
    """Route pour chiffrer un message AES."""
    return handle_encrypt_aes(request)

@router.post("/decrypt/AES", response_model=str)
async def decrypt(request: DecryptRequest):
    """Route pour déchiffrer un message AES."""
    return handle_decrypt_aes(request)


#********************************3DES*************************************************


@router.get("/generate-key/3DES", response_model=str)
async def generate_key():
    """Route pour générer une clé 3DES."""
    return generate_key_3des()

@router.post("/encrypt/3DES", response_model=str)
async def encrypt(request: EncryptRequest):
    """Route pour chiffrer un message 3DES."""
    return handle_encrypt_3des(request)

@router.post("/decrypt/3DES", response_model=str)
async def decrypt(request: DecryptRequest):
    """Route pour déchiffrer un message 3DES."""
    return handle_decrypt_3des(request)
