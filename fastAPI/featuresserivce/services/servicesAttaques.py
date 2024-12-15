from fastapi import HTTPException
from passlib.hash import md5_crypt, sha1_crypt, sha256_crypt
from typing import Optional
import hashlib
from models.dic import DictionaryWord, AttackRequest
from models.DicModel import Dictionary

def compute_hash(plain_password: str, salt: Optional[str], algorithm: str) -> str:
    """
    Compute hash for the password based on the given algorithm and salt.
    """
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
    # Utilisez .find_all() pour récupérer les entrées du dictionnaire
    words_cursor = await Dictionary.find_all().to_list()  # Conversion en liste pour itération asynchrone

    for entry in words_cursor:
        word = entry.password  # Accès aux données via les propriétés de l'objet
        try:
            if hash_algorithm == "md5" and salt:
                hashed_password = "$1$" + salt + "$" + hashed_password
            elif hash_algorithm == "sha1" and salt:
                hashed_password = "$sha1$1$" + salt + "$" + hashed_password
            elif hash_algorithm == "sha256" and salt:
                hashed_password = "$5$rounds=1000$" + salt + "$" + hashed_password
            
            computed_hash = compute_hash(word, salt, hash_algorithm)
            
            if computed_hash == hashed_password:
                return {"success": True, "password_found": word}
        except ValueError:
            continue
    return {"success": False, "message": "Password not found in the dictionary"}
