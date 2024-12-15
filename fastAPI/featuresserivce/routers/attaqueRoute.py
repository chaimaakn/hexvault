from fastapi import APIRouter, Query
from controleur.hashControleur import handle_hash_request,handle_hash_request_find

router = APIRouter()

@router.get("/hash")
async def get_hashed_password(password: str, algorithm: str):
    """
    Appelle la fonction contrôleur pour traiter la requête de hachage.
    """
    return handle_hash_request(password, algorithm)




@router.get("/hash/verif")
async def get_hashed_password_find(
    attaque: str = Query(..., description="Le mot de passe ou le hachage d'entrée"),
    algorithme: str = Query(..., description="L'algorithme utilisé pour traiter l'entrée"),
):
    """
    Point de terminaison pour vérifier un mot de passe ou un hachage basé sur une attaque donnée.

    Args:
        attaque (str): L'entrée à analyser (soit un mot de passe, soit un hachage).
        algorithme (str): L'algorithme utilisé pour le traitement (e.g., SHA256, RSA, etc.).

    Returns:
        dict: Résultat de la recherche ou erreur si non trouvé.
    """
    return await handle_hash_request_find(attaque, algorithme)
