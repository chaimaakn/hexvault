from beanie import Document
from pydantic import Field, root_validator,model_validator
from datetime import datetime
class PasswordFeature(Document):
    """
    Modèle représentant une fonctionnalité de gestion des mots de passe avec des champs spécifiques.
    """
    id_utilisateur: str = Field(..., description="Identifiant de l'utilisateur associé")
    nom: str = Field(
        ..., 
        description="Nom de la fonctionnalité",
        pattern="^(Attaque par brut force|Attaque par dictionnaire|Attaque dictionnaire amélioré|Attaque hybrid|HachageMot|Generate_key|encrypt|decrypt)$"
    )
    entree: str = Field(..., description="Entrée de l'opération (string)")
    sortie: str = Field(..., description="Sortie de l'opération (string)")
    key: str =  Field(..., description="Key public en cas d'encryption")
    type: str = Field(
        ..., 
        description="Type de l'opération",
        pattern="^(HtoM|MtoH|encrypt)$"   # HtoM les methodes ke type d'entree est un hachage et le type de sortie est un mot et MtoH sont les mots avec le type d'entrée est un mot et la sortie est une hachage
    )
    methode: str = None
    date_creation: datetime = Field(
        default_factory=datetime.utcnow, 
        description="Date et heure de création de l'enregistrement"
    )
    date_modification: datetime = Field(
        default_factory=datetime.utcnow, 
        description="Date et heure de dernière modification de l'enregistrement"
    )

    @model_validator(mode="after")
    def validate_methode_field(cls, values):
        """
        Valide que le champ 'methode' est requis pour les types 'HtoM' et 'encrypt'.
        """
        type_op = values.type
        methode = values.methode
        key=values.key

        if type_op in ['HtoM', 'encrypt'] and not methode:
            raise ValueError(
                "Le champ 'methode' est obligatoire pour les types 'HtoM' et 'encrypt'."
            )
        if type_op in['encrypt'] and not key:
            raise ValueError(
                "Le champ 'key' est obligatoire pour les types 'encrypt'."
            )   
        return values

    class Config:
        schema_extra = {
            "example": {
                "id_utilisateur": "user12345",
                "nom": "Attaque par brut force",
                "entree": "mot_de_passe_a_tester",
                "sortie": "mot_de_passe_trouve",
                "key":"cle",
                "type": "HtoM",
                "methode": "SHA256",
                "date_creation": "2024-12-14T12:34:56Z",
                "date_modification": "2024-12-14T12:34:56Z"
            }
        }
