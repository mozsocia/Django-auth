from django.urls import path, include
from .views import RegisterUser, UserList
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('allusers/', UserList.as_view(), name='allusers'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
