from django.urls import path, include
from .views import RegisterUser, UserList
from rest_framework.authtoken import views

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('api-token-auth/', views.obtain_auth_token),
    path('allusers/', UserList.as_view(), name='allusers'),
]
