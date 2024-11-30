from fastapi import APIRouter
from typing import List
from models.fncts import PasswordFeature
import controllers.controllersFcts as controller  

router = APIRouter()

@router.post("/create", response_model=PasswordFeature)
async def create_feature(feature: PasswordFeature):
    return await controller.create_feature(feature)

@router.get("/list", response_model=List[PasswordFeature])
async def list_features():
    return await controller.list_features()

@router.get("/{feature_id}", response_model=PasswordFeature)
async def get_feature(feature_id: str):
    return await controller.get_feature(feature_id)

@router.put("/modifie/{feature_id}", response_model=PasswordFeature)
async def update_feature(feature_id: str, updated_data: PasswordFeature):
    return await controller.update_feature(feature_id, updated_data)

@router.delete("/delete/{feature_id}")
async def delete_feature(feature_id: str):
    return await controller.delete_feature(feature_id)
