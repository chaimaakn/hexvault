from fastapi import HTTPException
import hashlib
from passlib.hash import md5_crypt
from passlib.hash import sha1_crypt
from passlib.hash import sha256_crypt
from models.dic import DictionaryWord,AttackRequest
