from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from pymongo.mongo_client import MongoClient
from models.users import Userhexvault  # Ajustez le chemin d'import selon votre structure de projet

# Configuration de l'application FastAPI
app = FastAPI(title="Mon Application")

# Configuration de la connexion à MongoDB
MONGO_URI = "mongodb+srv://xxxx/"#elle se trouve dans le .env aprés je vais la brancher ici
DATABASE_NAME = "hexvault"

@app.on_event("startup")
async def startup_event():
    """
    Fonction de démarrage pour initialiser la connexion MongoDB et Beanie
    """
    # Création du client MongoDB
    client = AsyncIOMotorClient(MONGO_URI)
    
    # Initialisation de Beanie avec vos modèles
    await init_beanie(
        database=client[DATABASE_NAME], 
        document_models=[
            Userhexvault,  # Ajoutez ici les autres modèles si vous en avez
        ]
    )

@app.on_event("shutdown")
async def shutdown_event():
    """
    Fonction de fermeture pour fermer proprement la connexion MongoDB
    """
    # Récupérer le client MongoDB
    client = AsyncIOMotorClient(MONGO_URI)
    client.close()

# Exemple de route pour la création d'utilisateur
from fastapi import HTTPException
from models.users import UserCreate

@app.post("/users/")
async def create_user(user: UserCreate):
    try:
        # Vérifier si l'utilisateur existe déjà
        existing_user_email = await Userhexvault.find_one(Userhexvault.email == user.email)
        existing_user_username = await Userhexvault.find_one(Userhexvault.username == user.username)
        
        if existing_user_email:
            raise HTTPException(status_code=400, detail="Un utilisateur avec cet email existe déjà")
        
        if existing_user_username:
            raise HTTPException(status_code=400, detail="Ce nom d'utilisateur est déjà pris")
        
        # Création de l'utilisateur
        new_user = await Userhexvault.create_user(
            nom=user.nom,
            prenom=user.prenom,
            username=user.username,
            email=user.email,
            password=user.password
        )
        
        return {"message": "Utilisateur créé avec succès", "user_id": str(new_user.id)}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Exemple de route pour la connexion
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Rechercher l'utilisateur par username
    user = await Userhexvault.find_one(Userhexvault.username == form_data.username)
    
    if not user:
        raise HTTPException(status_code=400, detail="Utilisateur non trouvé")
    
    # Vérifier le mot de passe
    if not user.verify_password(form_data.password):
        raise HTTPException(status_code=400, detail="Mot de passe incorrect")
    
    return {"access_token": "token_factice", "token_type": "bearer"}

# Configuration pour le lancement
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)