from typing import List, Optional
from beanie import Document
from pydantic import Field, validator

class PasswordFeature(Document):
    """
    Modèle représentant une fonctionnalité de gestion des mots de passe
    """
    nom: str = Field(..., description="Nom de la fonctionnalité")
    type: str = Field(
        ...,
        description="Type de fonctionnalité (attaque, cryptage, décryptage, test password)",
        pattern="^(attaque|cryptage|décryptage|test password)$"  # Utilisez `pattern` ici
    )
    dictionnaire: bool = Field(..., description="Utilise un dictionnaire ? (oui/non)")
    threads: bool = Field(..., description="Supporte les threads ? (oui/non)")
    fonctions_hachage: Optional[List[str]] = Field(
        default=None,
        description="Liste des fonctions de hachage utilisées (si applicable)"
    )

    class Config:
        schema_extra = {
            "example": {
                "nom": "Brute Force Attack",
                "type": "attaque",
                "dictionnaire": True,# si on la fait par les requete on fait pas la premiére lettre en majiscule
                "threads": True,
                "fonctions_hachage": ["md5", "sha1", "bcrypt"]
            }
        }

    @validator("fonctions_hachage", always=True)
    def validate_hash_functions(cls, v, values):
        """
        Valide les fonctions de hachage uniquement si le type est 'attaque'
        """
        if values.get("type") == "attaque" and not v:
            raise ValueError(
                "Les fonctions de hachage doivent être spécifiées pour une attaque."
            )
        if values.get("type") != "attaque" and v:
            raise ValueError(
                "Les fonctions de hachage ne sont pertinentes que pour les attaques."
            )
        return v
