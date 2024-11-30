from fastapi import APIRouter, HTTPException
from typing import List
from models.fncts import PasswordFeature

router = APIRouter()

@router.post("/create", response_model=PasswordFeature)
async def create_feature(feature: PasswordFeature):

    try:
        await feature.insert()
        return feature
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/list", response_model=List[PasswordFeature])
async def list_features():

    features = await PasswordFeature.find_all().to_list()
    return features

@router.get("/{feature_id}", response_model=PasswordFeature)
async def get_feature(feature_id: str):
  
    feature = await PasswordFeature.get(feature_id)
    if not feature:
        raise HTTPException(status_code=404, detail="Fonctionnalité non trouvée")
    return feature

@router.put("/modifie/{feature_id}", response_model=PasswordFeature)
async def update_feature(feature_id: str, updated_data: PasswordFeature):

    feature = await PasswordFeature.get(feature_id)
    if not feature:
        raise HTTPException(status_code=404, detail="Fonctionnalité non trouvée")

    for field, value in updated_data.dict().items():
        setattr(feature, field, value)

    await feature.save()
    return feature

@router.delete("/delete/{feature_id}")
async def delete_feature(feature_id: str):

    feature = await PasswordFeature.get(feature_id)
    if not feature:
        raise HTTPException(status_code=404, detail="Fonctionnalité non trouvée")

    await feature.delete()
    return {"message": "Fonctionnalité supprimée avec succès"}
