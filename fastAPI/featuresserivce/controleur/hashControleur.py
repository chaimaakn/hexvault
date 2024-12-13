from fastapi import HTTPException
from services.servicesHash import hash_password

def handle_hash_request(password: str, algorithm: str) -> dict:
    """
    Fonction contrôleur pour gérer la requête de hachage de mot de passe.
    Cette fonction interagit avec le service pour effectuer l'opération.
    """
    try:
        hashed_password = hash_password(password, algorithm)
        return {"algorithm": algorithm, "hashed_password": hashed_password}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
