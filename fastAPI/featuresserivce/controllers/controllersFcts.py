from fastapi import APIRouter, HTTPException
from typing import List
from ..models.fncts import PasswordFeature



async def delete_feature(feature_id: str):

    feature = await PasswordFeature.get(feature_id)
    if not feature:
        raise HTTPException(status_code=404, detail="Fonctionnalité non trouvée")

    await feature.delete()
    return {"message": "Fonctionnalité supprimée avec succès"}


async def update_feature(feature_id: str, updated_data: PasswordFeature):

    feature = await PasswordFeature.get(feature_id)
    if not feature:
        raise HTTPException(status_code=404, detail="Fonctionnalité non trouvée")

    for field, value in updated_data.dict().items():
        setattr(feature, field, value)

    await feature.save()
    return feature

async def get_feature(feature_id: str):
  
    feature = await PasswordFeature.get(feature_id)
    if not feature:
        raise HTTPException(status_code=404, detail="Fonctionnalité non trouvée")
    return feature

async def list_features():

    features = await PasswordFeature.find_all().to_list()
    return features

async def create_feature(feature: PasswordFeature):

    try:
        await feature.insert()
        return feature
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
