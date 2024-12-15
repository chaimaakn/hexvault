from pydantic import BaseModel

class DictionaryWord(BaseModel):
    word: str

class AttackRequest(BaseModel):
    hashed_password: str
    salt: str | None = None
    hash_algorithm: str  # "md5", "sha1", or "sha256"