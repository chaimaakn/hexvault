from django.urls import path
from .views import RegisterUserView,LoginUserView,DeleteUserView,update_password,list_users,get_user_by_id,update_username,deactivate_user

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('delete/<str:user_id>/', DeleteUserView.as_view(), name='delete_user'),
    path('users/<str:user_id>/update-password/', update_password, name='update-password'),
    path('users/', list_users, name='list-users'),
    path('users/<str:user_id>/', get_user_by_id, name='get-user-by-id'),
    path('users/<str:user_id>/update-username/', update_username, name='update-username'),
    path('users/<str:user_id>/deactivate/', deactivate_user, name='deactivate-user'),
    
    
    
]


