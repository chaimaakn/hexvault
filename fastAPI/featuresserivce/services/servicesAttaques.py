from fastapi import HTTPException
from passlib.hash import md5_crypt, sha1_crypt, sha256_crypt
from typing import Optional
import hashlib
from models.dic import DictionaryWord, AttackRequest
from models.DicModel import Dictionary
"""""
def compute_hash(plain_password: str, salt: Optional[str], algorithm: str) -> str:
    
    #Compute hash for the password based on the given algorithm and salt.
    
    if algorithm == "md5" and salt:
        return md5_crypt.using(salt=salt).hash(plain_password)
    elif algorithm == "md5":
        return hashlib.md5(plain_password.encode("utf-8")).hexdigest()
    elif algorithm == "sha1" and salt:
        return sha1_crypt.using(salt=salt).hash(plain_password)
    elif algorithm == "sha1":
        return hashlib.sha1(plain_password.encode("utf-8")).hexdigest()
    elif algorithm == "sha256" and salt:
        return sha256_crypt.using(salt=salt).hash(plain_password)
    elif algorithm == "sha256":
        return hashlib.sha256(plain_password.encode("utf-8")).hexdigest()
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")
# Exemple de fonction modifiée pour utiliser la syntaxe correcte

async def perform_dictionary_attack_logic(hashed_password: str, salt: str | None, hash_algorithm: str):
    # Utiliser async for pour itérer sur les documents sans charger tous les mots dans la mémoire
    async for entry in Dictionary.find({}):  # Pas besoin de .to_list(), on itère directement
        word = entry.password  # Assurez-vous que 'password' est bien un champ valide
        try:
            computed_hash = compute_hash(word, salt, hash_algorithm)

            # Comparer les hashes
            if computed_hash == hashed_password:
                return {"success": True, "password_found": word}
        except ValueError:
            continue

    return {"success": False, "message": "Password not found in the dictionary"}

   
    """
    
def compute_hash(plain_password: str, salt: Optional[str], algorithm: str) -> str:
    """
    Compute hash for the password based on the given algorithm and optional salt.
    Si le salt est fourni, il est utilisé pour hacher le mot de passe, sinon le hachage est effectué sans salt.
    """
    if algorithm == "md5":
        if salt:
            return md5_crypt.using(salt=salt).hash(plain_password)  # Avec salt
        return hashlib.md5(plain_password.encode("utf-8")).hexdigest()  # Sans salt
    elif algorithm == "sha1":
        if salt:
            return sha1_crypt.using(salt=salt).hash(plain_password)  # Avec salt
        return hashlib.sha1(plain_password.encode("utf-8")).hexdigest()  # Sans salt
    elif algorithm == "sha256":
        if salt:
            return sha256_crypt.using(salt=salt).hash(plain_password)  # Avec salt
        return hashlib.sha256(plain_password.encode("utf-8")).hexdigest()  # Sans salt
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")


async def perform_dictionary_attack_logic(hashed_password: str, salt: Optional[str], hash_algorithm: str):
    """
    Effectue une attaque par dictionnaire pour tester si le mot de passe haché est présent dans la base de données.
    Utilise l'algorithme de hachage spécifié, en tenant compte du salt s'il est fourni.
    """
    async for entry in Dictionary.find({}):  # Itération sur les documents sans les charger en mémoire
        word = entry.password  # Assurez-vous que 'password' est bien un champ valide dans la base
        try:
            # Calcule le hash du mot actuel en fonction de l'algorithme et du salt
            computed_hash = compute_hash(word, salt, hash_algorithm)

            # Si le hash calculé correspond au mot de passe haché, retourner le mot trouvé
            if computed_hash == hashed_password:
                return {"success": True, "password_found": word}
        except ValueError:
            continue  # En cas d'erreur (par exemple, un hash non valide), on continue avec le mot suivant

    return {"success": False, "message": "Password not found in the dictionary"}
