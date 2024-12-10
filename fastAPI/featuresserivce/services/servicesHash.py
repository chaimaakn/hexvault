import hashlib

def hash_password(password: str, algorithm: str) -> str:
    """
    Hache un mot de passe en utilisant l'algorithme spécifié.
    """
    try:
        if algorithm == "sha1":
            return hashlib.sha1(password.encode()).hexdigest()
        elif algorithm == "md5":
            return hashlib.md5(password.encode()).hexdigest()
        elif algorithm == "sha256":
            return hashlib.sha256(password.encode()).hexdigest()
        else:
            raise ValueError("Algorithme non supporté")
    except Exception as e:
        raise ValueError(f"Erreur lors du hachage : {str(e)}")
