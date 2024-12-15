from fastapi import APIRouter, Query
from controleur.hashControleur import handle_hash_request,handle_hash_request_find
from models.dic import AttackRequest,DictionaryWord
from models.DicModel import Dictionary
from services.servicesAttaques import perform_dictionary_attack_logic
from fastapi import HTTPException
from beanie import  PydanticObjectId

router = APIRouter()

@router.get("/hash")
async def get_hashed_password(password: str, algorithm: str):
    """
    Appelle la fonction contrôleur pour traiter la requête de hachage.
    """
    return handle_hash_request(password, algorithm)




@router.get("/hash/verif")
async def get_hashed_password_find(
    attaque: str = Query(..., description="Valeur à vérifier (attaque)"),
    algorithme: str = Query(..., description="Algorithme utilisé"),
    id_utilisateur: str = Query(..., description="ID de l'utilisateur")
):
    """
    Route pour gérer les requêtes de hachage avec vérification utilisateur.
    """
    return await handle_hash_request_find(attaque, algorithme,id_utilisateur)



@router.post("/Dictionnaire")
async def dictionary_attack(request: AttackRequest):
    try:
        # Appel de la fonction qui effectue l'attaque par dictionnaire
        result = await perform_dictionary_attack_logic(request.hashed_password, request.salt, request.hash_algorithm)
        
        # Vérifiez si le résultat indique une erreur (par exemple, "success": False)
        if not result["success"]:
            raise HTTPException(status_code=404, detail=result["message"])
        
        return result  # Retourne le résultat de l'attaque par dictionnaire
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error in hash computation: {str(e)}")
    except Exception as e:
        # Capture toute autre exception et renvoyer une erreur 500 pour l'erreur interne
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
    


@router.get("/word/{word_id}")
async def get_word(word_id: str):
    try:
        # Rechercher un mot dans la collection par son ID
        word = await Dictionary.get(PydanticObjectId(word_id))
        
        if word:
            return {"word": word.password}  # Retourner le mot
        else:
            raise HTTPException(status_code=404, detail="Word not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
