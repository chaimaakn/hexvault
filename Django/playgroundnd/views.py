from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import CustomUser

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
