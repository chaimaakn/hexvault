from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from models.users import Userhexvault, UserCreate, UserLogin
import controllers.controllerUser as controlleuser

router = APIRouter()


@router.post("/register/")
async def register_user(user: UserCreate):
    return await controlleuser.create_user(user)


#Rajouter l'autentification
@router.post("/login")
async def login_user(form_data: UserLogin):
    return await controlleuser.login_user(form_data)

