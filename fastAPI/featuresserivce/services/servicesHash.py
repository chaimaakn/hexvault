import hashlib
from models.fncts import PasswordFeature
from fastapi import APIRouter, HTTPException

def hash_password(password: str, algorithm: str) -> str:
    """
    Hache un mot de passe en utilisant l'algorithme spécifié.
    """
    try:
        if algorithm == "sha1":
            return hashlib.sha1(password.encode()).hexdigest()
        elif algorithm == "md5":
            return hashlib.md5(password.encode()).hexdigest()
        elif algorithm == "sha256":
            return hashlib.sha256(password.encode()).hexdigest()
        else:
            raise ValueError("Algorithme non supporté")
    except Exception as e:
        raise ValueError(f"Erreur lors du hachage : {str(e)}")




async def find_matching_feature(password: str, algorithm: str) -> dict:
    """
    Recherche une fonctionnalité correspondante dans la base de données pour MtH et HtM.

    Args:
        password (str): Texte ou hachage à vérifier.
        algorithm (str): Algorithme utilisé pour hacher ou comparer.

    Returns:
        dict: Résultat de la correspondance.
    """
    # Recherche pour MtH (Mapping Texte → Hash)
    mth_match = await PasswordFeature.find_one(
        {"type": "MtoH", "sortie": password, "methode": algorithm}
    )
    if mth_match:
        return {
            "type": "MtoH",
            "matched_functionality": mth_match.nom,
            "original_input": mth_match.entree,
        }

    # Recherche pour HtM (Hash → Texte)
    htm_match = await PasswordFeature.find_one(
        {"type": "HtoM", "entree": password, "methode": algorithm}
    )
    if htm_match:
        return {
            "type": "HtoM",
            "matched_functionality": htm_match.nom,
            "hash_output": htm_match.sortie,
        }

    # Si aucune correspondance trouvée
    raise ValueError("No match found for the provided input and algorithm.")
