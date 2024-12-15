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
    attaque: str = Query(..., description="Valeur à vérifier (attaque)"),
    algorithme: str = Query(..., description="Algorithme utilisé"),
    id_utilisateur: str = Query(..., description="ID de l'utilisateur")
):
    """
    Route pour gérer les requêtes de hachage avec vérification utilisateur.
    """
    return await handle_hash_request_find(attaque, algorithme, id_utilisateur)