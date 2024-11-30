import sys
import os
from fastapi import FastAPI
from .routers.userRoute import router as user_router



app = FastAPI(title="User Service")


router = user_router
app.include_router(user_router, prefix="/users", tags=["Users"])

@app.get("/")
async def root():
    return {"message": "Bienvenue dans le User Service"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8001)
