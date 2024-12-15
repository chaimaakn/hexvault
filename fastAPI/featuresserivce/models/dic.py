from pydantic import BaseModel
from typing import Optional
class DictionaryWord(BaseModel):
    word: str

class AttackRequest(BaseModel):
    hashed_password: str
    salt: Optional[str] = None  # Le sel peut être absent pour certains algorithmes
    hash_algorithm: str  # md5, sha1, sha256, etc.