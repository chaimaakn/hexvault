from fastapi import FastAPI, HTTPException, APIRouter, Depends
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import hashlib
import os
from passlib.hash import md5_crypt
from passlib.hash import sha1_crypt
from passlib.hash import sha256_crypt
from fastapi import HTTPException
import hashlib
from passlib.hash import md5_crypt
from passlib.hash import sha1_crypt
from passlib.hash import sha256_crypt
from models.dic import DictionaryWord,AttackRequest

def compute_hash(plain_password: str, salt: str | None, algorithm: str) -> str:
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
async def perform_dictionary_attack_logic(hashed_password: str, salt: str | None, hash_algorithm: str):
    words_cursor = db["dictionaries"].find({})
    async for entry in words_cursor:
        word = entry["word"]
        try:
            if hash_algorithm == "md5" and salt:
                hashed_password="$1$" + salt + "$"+hashed_password
            elif  hash_algorithm == "sha1" and salt:
                hashed_password="$sha1$1$"+salt+"$"+hashed_password
            elif  hash_algorithm == "sha256" and salt:
                hashed_password="$5$rounds=1000$"+salt+"$"+hashed_password
            computed_hash = compute_hash(word, salt, hash_algorithm)
            if computed_hash == hashed_password:
                return {"success": True, "password_found": word}
        except ValueError:
            continue
    return {"success": False, "message": "Password not found in the dictionary"}