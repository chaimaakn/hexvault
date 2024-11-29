from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from pymongo.mongo_client import MongoClient
from models.users import Userhexvault  
from dotenv import load_dotenv
import os
load_dotenv()
from routers.userRoute import router as userRoute
from routers.fnctsRoute import router as fnctsRoute
from routers.historiqueRoute import router as historiqueRoute
from routers.attaqueRoute import router as attaqueRoute

app = FastAPI(title="hexvault")

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
SERVER_HOST=os.getenv("SERVER_HOST")
SERVER_PORT=os.getenv("SERVER_PORT")

@app.on_event("startup")
async def startup_event():
    client = AsyncIOMotorClient(MONGO_URI)
    await init_beanie(
        database=client[DATABASE_NAME], 
        document_models=[
            Userhexvault,  
        ]
    )

@app.on_event("shutdown")
async def shutdown_event():
    client = AsyncIOMotorClient(MONGO_URI)
    client.close()

app.include_router(userRoute, prefix="/user", tags=["Utilisateur"])
app.include_router(fnctsRoute, prefix="/fonctions", tags=["fonctions"])
app.include_router(historiqueRoute, prefix="/history", tags=["history"])
app.include_router(attaqueRoute, prefix="/attaque", tags=["attaque"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=SERVER_HOST, port=SERVER_PORT)