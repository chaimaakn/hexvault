from fastapi import FastAPI
from dotenv import load_dotenv
import os
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from pymongo.mongo_client import MongoClient
# Importer le routeur depuis le chemin relatif
from routers.fnctsRoute import router as feature_router
from routers.encryptRoute import router as encrypt_router
from models.fncts import PasswordFeature
load_dotenv()

app = FastAPI(title="Features Service")

# Exportez le routeur
router = feature_router

SERVER_HOST = os.getenv("SERVER_HOST")
SERVER_PORT = os.getenv("SERVER_PORT")
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

@app.on_event("startup")
async def startup_event():
    client = AsyncIOMotorClient(MONGO_URI)
    await init_beanie(
        database=client[DATABASE_NAME], 
        document_models=[
            
            PasswordFeature
            
            
              
        ]
    )
@app.on_event("shutdown")
async def shutdown_event():
    client = AsyncIOMotorClient(MONGO_URI)
    client.close()
    
# Monter le router des fonctionnalités
app.include_router(feature_router, prefix="/features", tags=["Features"])
app.include_router(encrypt_router, prefix="/encrypt", tags=["encryption"])
@app.get("/")
async def root():
    return {"message": "Bienvenue dans le Features Service!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=SERVER_HOST, port=int(SERVER_PORT))