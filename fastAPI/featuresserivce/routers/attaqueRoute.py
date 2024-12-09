from fastapi import APIRouter, HTTPException
from services.servicesHash import hash_password

router = APIRouter()

@router.get("/hash")
async def get_hashed_password(password: str, algorithm: str):
    try:
        hashed_password = hash_password(password, algorithm)
        return {"algorithm": algorithm, "hashed_password": hashed_password}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
