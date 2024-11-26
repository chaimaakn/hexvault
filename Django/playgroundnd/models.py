import re
import secrets
import hashlib
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import validate_email, RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.models import Group, Permission


class EmailConfirmationToken(models.Model):
    """
    Modèle pour gérer les tokens de confirmation d'email
    """
    user = models.OneToOneField(
        'CustomUser', 
        on_delete=models.CASCADE, 
        related_name='email_confirmation_token'
    )
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    is_confirmed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """
        Définit automatiquement la date d'expiration
        """
        if not self.expires_at:
            self.expires_at = timezone.now() + timezone.timedelta(hours=24)
        super().save(*args, **kwargs)

    def is_valid(self):
        """
        Vérifie si le token est encore valide
        """
        return (not self.is_confirmed and 
                timezone.now() <= self.expires_at)

    def send_confirmation_email(self, request):
        """
        Envoie un email de confirmation
        """
        # Construire l'URL de confirmation
        confirmation_url = request.build_absolute_uri(
            reverse('email_confirmation', kwargs={'token': str(self.token)})
        )

        # Préparer le contenu de l'email
        context = {
            'user': self.user,
            'confirmation_url': confirmation_url,
            'expiration_hours': 24
        }

        # Rendu du template HTML
        html_message = render_to_string(
            'emails/email_confirmation.html', #a changer
            context
        )
        
        # Version texte brut
        plain_message = strip_tags(html_message)

        # Envoi de l'email
        send_mail(
            'Confirmez votre adresse email',
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [self.user.email],
            html_message=html_message,
            fail_silently=False,
        )

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Modèle utilisateur personnalisé avec des fonctionnalités de sécurité avancées
    """
    # Validateurs
    username_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9_]+$',
        message="Le nom d'utilisateur ne peut contenir que des lettres, chiffres et underscores"
    )

    # Champs principaux
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        max_length=50, 
        unique=True, 
        validators=[username_validator],
        help_text="Choisissez un nom d'utilisateur unique"
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    # Champs de sécurité
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_email_confirmed = models.BooleanField(default=False)
    
    # Métadonnées temporelles
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)
    
    # Sécurité du mot de passe
    password_salt = models.CharField(max_length=64, blank=True)
    password_hash = models.CharField(max_length=256)
    
    # Gestion des tentatives de connexion
    failed_login_attempts = models.IntegerField(default=0)
    lockout_time = models.DateTimeField(null=True, blank=True)
    # Remplacez le champ `groups` pour éviter les conflits
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",
        blank=True,
        help_text="Les groupes auxquels l'utilisateur appartient."
    )
    # Remplacez le champ `user_permissions` pour éviter les conflits
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",
        blank=True,
        help_text="Les permissions spécifiques attribuées à cet utilisateur."
    )
    # Configuration du modèle
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username

    def clean(self):
        """
        Validation globale
        """
        # Validation de l'email
        try:
            validate_email(self.email)
        except ValidationError:
            raise ValidationError("Email invalide")
        
        # Validation du username
        self.validate_username()
        
        # Validation du mot de passe
        if hasattr(self, '_password'):
            self.validate_password_strength(self._password)

    def validate_username(self):
        """
        Valide le username
        """
        if len(self.username) < 3:
            raise ValidationError("Le nom d'utilisateur doit faire au moins 3 caractères")
        
        if len(self.username) > 50:
            raise ValidationError("Le nom d'utilisateur ne peut pas dépasser 50 caractères")
        
        # Vérifier l'unicité
        if CustomUser.objects.exclude(pk=self.pk).filter(username=self.username).exists():
            raise ValidationError("Ce nom d'utilisateur est déjà utilisé")

    def validate_password_strength(self, password):
        """
        Vérifie la force du mot de passe
        """
        if len(password) < 12:
            raise ValidationError("Le mot de passe doit faire au moins 12 caractères")
        
        if not re.search(r'[A-Z]', password):
            raise ValidationError("Le mot de passe doit contenir au moins une majuscule")
        
        if not re.search(r'[a-z]', password):
            raise ValidationError("Le mot de passe doit contenir au moins une minuscule")
        
        if not re.search(r'\d', password):
            raise ValidationError("Le mot de passe doit contenir au moins un chiffre")
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError("Le mot de passe doit contenir au moins un caractère spécial")

    def generate_salt(self):
        """
        Génère un sel unique pour le hachage du mot de passe
        """
        return secrets.token_hex(32)  # 64 caractères

    def hash_password(self, password):
        """
        Hache le mot de passe avec un sel unique
        """
        # Générer un nouveau sel
        self.password_salt = self.generate_salt()
        
        # Concaténer le mot de passe avec le sel
        salted_password = f"{password}{self.password_salt}"
        
        # Hachage en utilisant SHA-256
        self.password_hash = hashlib.sha256(salted_password.encode()).hexdigest()

    def check_password(self, raw_password):
        """
        Vérifie si le mot de passe correspond au hash
        """
        # Recréer le hachage avec le sel existant
        salted_password = f"{raw_password}{self.password_salt}"
        hashed_attempt = hashlib.sha256(salted_password.encode()).hexdigest()
        
        # Comparer avec le hash existant
        return hashed_attempt == self.password_hash

    def set_password(self, raw_password):
        """
        Méthode pour définir un nouveau mot de passe
        """
        # Valider la force du mot de passe
        self.validate_password_strength(raw_password)
        
        # Hacher le mot de passe
        self.hash_password(raw_password)
        
        # Réinitialiser les tentatives de connexion
        self.reset_failed_attempts()
        
        # Stocker temporairement le mot de passe pour validation
        self._password = raw_password

    def increment_failed_attempts(self):
        """
        Incrémente les tentatives de connexion échouées
        """
        self.failed_login_attempts += 1
        
        # Verrouiller le compte après 5 tentatives
        if self.failed_login_attempts >= 5:
            self.lockout_time = timezone.now() + timezone.timedelta(minutes=15)
            self.is_active = False

    def reset_failed_attempts(self):
        """
        Réinitialise les tentatives de connexion
        """
        self.failed_login_attempts = 0
        self.lockout_time = None
        self.is_active = True

    def generate_unique_username(self, base_username=None):
        """
        Génère un username unique
        """
        if base_username is None:
            base_username = f"{self.first_name.lower()}{self.last_name.lower()}"
        
        # Nettoyer le username de base
        base_username = re.sub(r'[^a-zA-Z0-9_]', '', base_username)
        
        # Générer un username unique
        username = base_username
        counter = 1
        while CustomUser.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1
        
        return username

    def generate_email_confirmation_token(self, request):
        """
        Génère un nouveau token de confirmation d'email
        """
        # Supprimer les anciens tokens
        EmailConfirmationToken.objects.filter(user=self).delete()
        
        # Créer un nouveau token
        token = EmailConfirmationToken.objects.create(user=self)
        
        # Envoyer l'email de confirmation
        token.send_confirmation_email(request)
        
        return token

    @property
    def full_name(self):
        """
        Retourne le nom complet
        """
        return f"{self.first_name} {self.last_name}"

    @property
    def is_locked(self):
        """
        Vérifie si le compte est verrouillé
        """
        return (self.lockout_time and 
                self.lockout_time > timezone.now())


    @classmethod
    def create_user(cls, first_name, last_name, email, password, username=None, request=None):
        """
        Méthode de création d'utilisateur avec génération automatique de username
        et envoi de confirmation d'email
        """
        user = cls(
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        # Générer un username si non fourni
        if username is None:
            username = user.generate_unique_username()

        user.username = username
        user.set_password(password)
        user.save()

        # Générer un token de confirmation d'email si request est fourni
        """""
        if request is not None:
            user.generate_email_confirmation_token(request)
       """
        return user
