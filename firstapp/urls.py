from django.urls import path

from .views import *
from . import views


urlpatterns = [
    path('hello/', hello_view, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
