from fastapi import HTTPException
from services.servicesHash import hash_password
from services.servicesHash import find_matching_feature
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

async def handle_hash_request_find(password: str, algorithm: str) -> dict:
    """
    Fonction contrôleur pour gérer la requête de hachage de mot de passe.
    Interagit avec le service pour effectuer l'opération.

    Args:
        password (str): Mot de passe ou hachage à vérifier.
        algorithm (str): Algorithme utilisé (e.g., SHA256, MD5).

    Returns:
        dict: Résultat de la correspondance ou erreur.
    """
    try:
        return await find_matching_feature(password, algorithm)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
