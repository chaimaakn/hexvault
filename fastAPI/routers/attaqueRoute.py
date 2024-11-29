import hashlib
from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/attack",
    tags=["Attack"],
    responses={404: {"description": "Not Found"}},
)

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

@router.get("/hash")
async def get_hashed_password(password: str, algorithm: str):

    try:
        hashed_password = hash_password(password, algorithm)
        return {"algorithm": algorithm, "hashed_password": hashed_password}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
