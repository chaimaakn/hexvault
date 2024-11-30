from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Importer le routeur depuis le chemin relatif
from .routers.fnctsRoute import router as feature_router

load_dotenv()

app = FastAPI(title="Features Service")

# Exportez le routeur
router = feature_router

SERVER_HOST = os.getenv("SERVER_HOST")
SERVER_PORT = os.getenv("SERVER_PORT")

# Monter le router des fonctionnalités
app.include_router(feature_router, prefix="/features", tags=["Features"])

@app.get("/")
async def root():
    return {"message": "Bienvenue dans le Features Service!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=SERVER_HOST, port=int(SERVER_PORT))