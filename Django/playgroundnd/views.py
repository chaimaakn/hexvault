from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.utils import timezone
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password

@method_decorator(csrf_exempt, name='dispatch')
class RegisterUserView(View):
    def post(self, request):
        try:
            # Tenter de parser les données reçues en JSON
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                return JsonResponse({
                    'success': False,
                    'error': 'Données invalides. Un format JSON est attendu.'
                }, status=400)

            # Validation des champs requis
            required_fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password']
            missing_fields = [field for field in required_fields if not data.get(field)]
            if missing_fields:
                return JsonResponse({
                    'success': False,
                    'error': 'Certains champs sont manquants.',
                    'missing_fields': missing_fields
                }, status=400)

            # Vérification des mots de passe
            if data['password'] != data['confirm_password']:
                return JsonResponse({
                    'success': False,
                    'error': 'Les mots de passe ne correspondent pas.'
                }, status=400)

            # Appeler la méthode de classe `create_user` pour créer l'utilisateur
            try:
                username = data.get('username', None)  # Si `username` n'est pas fourni, utilisez None
                user = CustomUser.create_user(
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    email=data['email'],
                    password=data['password'],
                    username=username,
                    request=request  # Ajout pour le token d'email si nécessaire
                )

                # Si l'utilisateur a été créé avec succès, retourner une réponse
                return JsonResponse({
                    'success': True,
                    'message': 'Utilisateur créé avec succès.',
                    'user_id': str(user.id),
                    'username': user.username
                }, status=201)

            except Exception as e:
                return JsonResponse({
                    'success': False,
                    'error': 'Une erreur est survenue lors de la création de l\'utilisateur.',
                    'details': str(e)
                }, status=400)

        except Exception as e:
            # Capture des exceptions globales
            return JsonResponse({
                'success': False,
                'error': 'Erreur interne du serveur.',
                'details': str(e)
            }, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class LoginUserView(View):
    def post(self, request):
        try:
            # Charger les données JSON
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            # Vérifier que les champs requis sont présents
            if not email or not password:
                return JsonResponse({
                    'success': False,
                    'error': 'Email et mot de passe sont requis.'
                }, status=400)

            # Vérifier si un utilisateur correspond à l'email
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'error': 'Aucun utilisateur ne correspond à cet email.'
                }, status=404)

            # Vérifier le mot de passe
            if not user.check_password(password):
                user.increment_failed_attempts()  # Incrémenter les tentatives échouées
                user.save()
                return JsonResponse({
                    'success': False,
                    'error': 'Mot de passe incorrect.'
                }, status=401)

            # Vérifier si le compte est actif
            if not user.is_active:
                return JsonResponse({
                    'success': False,
                    'error': 'Compte désactivé ou verrouillé.'
                }, status=403)

            # Réinitialiser les tentatives échouées et enregistrer la dernière connexion
            user.reset_failed_attempts()
            user.last_login = timezone.now()
            user.save()

            return JsonResponse({
                'success': True,
                'message': 'Connexion réussie.',
                'user': {
                    'id': str(user.id),
                    'username': user.username,
                    'email': user.email,
                    'full_name': user.full_name
                }
            }, status=200)

        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': 'Erreur interne du serveur.',
                'details': str(e)
            }, status=500)
@method_decorator(csrf_exempt, name='dispatch')
class DeleteUserView(View):
    def delete(self, request, user_id):
        try:
            # Afficher tous les utilisateurs pour vérification
            print("Tous les utilisateurs :")
            print(CustomUser.objects.all())

            # Vérifier le type et la valeur de user_id
            print("Type de user_id:", type(user_id))
            print("Valeur de user_id:", user_id)

            # Essayez de filtrer plutôt que de get
            users = CustomUser.objects.filter(id=user_id)
            print("Utilisateurs filtrés:", users)

            # Vérifier si l'utilisateur existe
            try:
                user = CustomUser.objects.get(id=user_id)
            except CustomUser.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'error': 'Utilisateur introuvable.'
                }, status=404)

            # Supprimer l'utilisateur de la base de données
            user.delete()

            return JsonResponse({
                'success': True,
                'message': f"L'utilisateur avec l'UUID {user_id} a été supprimé avec succès."
            }, status=200)

        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': 'Erreur interne du serveur.',
                'details': str(e)
            }, status=500)

@csrf_exempt
def update_password(request, user_id):
    """
    Met à jour le mot de passe d'un utilisateur via son ID.
    """
    if request.method != 'PUT':  # On vérifie que la méthode utilisée est PUT
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)

    # Récupérer l'utilisateur
    user = get_object_or_404(CustomUser, id=user_id)

    try:
        # Charger les données JSON envoyées dans la requête
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Requête invalide, données JSON mal formatées'}, status=400)

    # Vérifier si le champ 'new_password' est présent
    if 'new_password' not in data or not data['new_password']:
        return JsonResponse({'error': 'Le champ "new_password" est requis'}, status=400)

    new_password = data['new_password']

    # Appliquer le nouveau mot de passe en le hachant
    user.password = make_password(new_password)

    try:
        user.save()  # Sauvegarder le nouveau mot de passe
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'message': 'Mot de passe mis à jour avec succès'}, status=200)
@csrf_exempt
def update_username(request, user_id):
    """
    Met à jour le nom d'utilisateur d'un utilisateur via son ID.
    """
    if request.method != 'PUT':  # Vérifier que la méthode est PUT
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)

    # Récupérer l'utilisateur
    user = get_object_or_404(CustomUser, id=user_id)

    try:
        # Charger les données JSON envoyées dans la requête
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Requête invalide, données JSON mal formatées'}, status=400)

    # Vérifier si le champ 'new_username' est présent
    if 'new_username' not in data or not data['new_username']:
        return JsonResponse({'error': 'Le champ "new_username" est requis'}, status=400)

    new_username = data['new_username']

    # Vérifier si le nom d'utilisateur existe déjà
    if CustomUser.objects.filter(username=new_username).exists():
        return JsonResponse({'error': 'Ce nom d\'utilisateur est déjà pris'}, status=400)

    # Mettre à jour le nom d'utilisateur
    user.username = new_username

    try:
        user.save()  # Sauvegarder le nouveau nom d'utilisateur
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'message': 'Nom d\'utilisateur mis à jour avec succès'}, status=200)

def list_users(request):
    """
    Vue fonctionnelle pour afficher tous les utilisateurs.
    """
    users = CustomUser.objects.values(  # Récupérer les utilisateurs et leurs champs
        'id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined'
    )
    return JsonResponse(list(users), safe=False)  

def get_user_by_id(request, user_id):
    """
    Récupère les informations d'un utilisateur via son ID.
    """
    user = get_object_or_404(CustomUser, id=user_id)  # Récupère l'utilisateur ou renvoie une 404 si non trouvé

    user_data = {
        'id': str(user.id),
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'is_active': user.is_active,
        'date_joined': user.date_joined.strftime('%Y-%m-%d %H:%M:%S'),
    }

    return JsonResponse(user_data)

@csrf_exempt
def deactivate_user(request, user_id):
    """
    Désactive un utilisateur en mettant son champ is_active à False via son ID.
    """
    if request.method != 'PUT':  # Vérifier que la méthode est PUT
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)

    # Récupérer l'utilisateur
    user = get_object_or_404(CustomUser, id=user_id)

    # Vérifier si l'utilisateur est déjà inactif
    if not user.is_active:
        return JsonResponse({'error': 'L\'utilisateur est déjà inactif'}, status=400)

    # Mettre à jour le champ is_active
    user.is_active = False

    try:
        user.save()  # Sauvegarder la modification
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'message': 'Utilisateur désactivé avec succès'}, status=200)
