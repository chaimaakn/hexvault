from fastapi import HTTPException
from models.dic import AttackRequest
from services.servicesAttaques import perform_dictionary_attack_logic,dic_amelioer,hybrid_attack_logic,brute_force_attack


async def handle_dicAttaque(request: AttackRequest) -> str:
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
async def handle_bruteForce(request: AttackRequest) -> str:
    try:
        # Appel de la fonction qui effectue l'attaque par dictionnaire
        result = await brute_force_attack(request.hashed_password, request.salt, request.hash_algorithm)
        
        # Vérifiez si le résultat indique une erreur (par exemple, "success": False)
        if not result["success"]:
            raise HTTPException(status_code=404, detail=result["message"])
        
        return result  # Retourne le résultat de l'attaque par dictionnaire
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error in hash computation: {str(e)}")
    except Exception as e:
        # Capture toute autre exception et renvoyer une erreur 500 pour l'erreur interne
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
async def handle_dicAmeliorer(request: AttackRequest) -> str:
    try:
        # Appel de la fonction qui effectue l'attaque par dictionnaire
        result = await dic_amelioer(request.hashed_password, request.salt, request.hash_algorithm)
        
        # Vérifiez si le résultat indique une erreur (par exemple, "success": False)
        if not result["success"]:
            raise HTTPException(status_code=404, detail=result["message"])
        
        return result  # Retourne le résultat de l'attaque par dictionnaire
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error in hash computation: {str(e)}")
    except Exception as e:
        # Capture toute autre exception et renvoyer une erreur 500 pour l'erreur interne
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
    
    
async def handle_hybrid(request: AttackRequest) -> str:
    
    try:
        # Appel de la fonction qui effectue l'attaque par dictionnaire
        result = await hybrid_attack_logic(request.hashed_password, request.salt, request.hash_algorithm)
        
        # Vérifiez si le résultat indique une erreur (par exemple, "success": False)
        if not result["success"]:
            raise HTTPException(status_code=404, detail=result["message"])
        
        return result  # Retourne le résultat de l'attaque par dictionnaire
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error in hash computation: {str(e)}")
    except Exception as e:
        # Capture toute autre exception et renvoyer une erreur 500 pour l'erreur interne
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
    