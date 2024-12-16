from fastapi import HTTPException
from passlib.hash import md5_crypt, sha1_crypt, sha256_crypt
from typing import Optional
import hashlib
from models.dic import DictionaryWord, AttackRequest
from models.DicModel import Dictionary
import itertools

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
            return sha1_crypt.using(salt=salt).hash(plain_password,rounds=1)  # Avec salt
        return hashlib.sha1(plain_password.encode("utf-8")).hexdigest()  # Sans salt
    elif algorithm == "sha256":
        if salt:
            return sha256_crypt.using(salt=salt).hash(plain_password,rounds=1000)  # Avec salt
        return hashlib.sha256(plain_password.encode("utf-8")).hexdigest()  # Sans salt
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")


async def perform_dictionary_attack_logic(hashed_password: str, salt: Optional[str], hash_algorithm: str):
    """
    Effectue une attaque par dictionnaire pour tester si le mot de passe haché est présent dans la base de données.
    Utilise l'algorithme de hachage spécifié, en tenant compte du salt s'il est fourni.
    """
    if hash_algorithm == "md5" and salt:
                hashed_password="$1$" + salt + "$"+hashed_password
    elif  hash_algorithm == "sha1" and salt:
        hashed_password="$sha1$1$"+salt+"$"+hashed_password
    elif  hash_algorithm == "sha256" and salt:
        hashed_password="$5$rounds=1000$"+salt+"$"+hashed_password
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

def apply_transformations(base_password):
    """Applique différentes transformations sur un mot de passe de base.pour l'attaque de dictionnaire ameliorer"""
    # Vous pouvez ajouter autant de transformations que vous le souhaitez
    transformations = [
        base_password.upper(),
        base_password.lower(),
        base_password.capitalize(),
        base_password + "123",
        base_password + "!",
        "123" + base_password,
        "!"+ base_password,
    ]
    return transformations
def brute_force_extension(base_password, charset, max_length=2):
    """Génère des extensions de force brute pour un mot de base."""
    for length in range(1, max_length + 1):
        for combo in itertools.product(charset, repeat=length):
            yield base_password + ''.join(combo)

async def dic_amelioer(hashed_password: str, salt: Optional[str], hash_algorithm: str):
    """ Effectue une attaque par dictionnaire pour tester si le mot de passe haché est présent dans la base de données.
    Utilise l'algorithme de hachage spécifié, en tenant compte du salt s'il est fourni.
    """
    if hash_algorithm == "md5" and salt:
                hashed_password="$1$" + salt + "$"+hashed_password
    elif  hash_algorithm == "sha1" and salt:
        hashed_password="$sha1$1$"+salt+"$"+hashed_password
    elif  hash_algorithm == "sha256" and salt:
        hashed_password="$5$rounds=1000$"+salt+"$"+hashed_password
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
    async for entry in Dictionary.find({}):  # Itération sur les documents sans les charger en mémoire
        word = entry.password 
        transformations = apply_transformations(word)
        for password in transformations:
            try:
                if compute_hash(password, salt, hash_algorithm) == hashed_password:
                    return {"success": True, "password_found": password}
            except ValueError:
                continue  # En cas d'erreur (par exemple, un hash non valide), on continue avec le mot suivant
    return {"success": False, "message": "Password not found in the dictionary"}
async def hybrid_attack_logic(hashed_password: str, salt: Optional[str], hash_algorithm: str):
    """ Effectue une attaque par dictionnaire pour tester si le mot de passe haché est présent dans la base de données.
    Utilise l'algorithme de hachage spécifié, en tenant compte du salt s'il est fourni.
    """
    charset="0123456789!@#"
    if hash_algorithm == "md5" and salt:
                hashed_password="$1$" + salt + "$"+hashed_password
    elif  hash_algorithm == "sha1" and salt:
        hashed_password="$sha1$1$"+salt+"$"+hashed_password
    elif  hash_algorithm == "sha256" and salt:
        hashed_password="$5$rounds=1000$"+salt+"$"+hashed_password
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
    async for entry in Dictionary.find({}):  # Itération sur les documents sans les charger en mémoire
        word = entry.password 
        transformations = apply_transformations(word)
        for password in transformations:
            try:
                if compute_hash(password, salt, hash_algorithm) == hashed_password:
                    return {"success": True, "password_found": password}
            except ValueError:
                continue  # En cas d'erreur (par exemple, un hash non valide), on continue avec le mot suivant
        # Appliquer la force brute avec extensions sur chaque transformation
        for password in transformations:
            for extended_password in brute_force_extension(password, charset):
                if compute_hash(extended_password, salt, hash_algorithm) == hashed_password:
                    return {"success": True, "password_found": extended_password}
    return {"success": False, "message": "Password not found in the dictionary"}