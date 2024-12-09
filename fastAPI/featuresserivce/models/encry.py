from pydantic import BaseModel

class EncryptRequest(BaseModel):
    """Modèle pour les requêtes de chiffrement."""
    message: str
    key: str

class DecryptRequest(BaseModel):
    """Modèle pour les requêtes de déchiffrement."""
    encrypted_message: str
    key: str
