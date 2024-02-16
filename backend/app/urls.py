from . import views
from django.urls import path

urlpatterns = [
    path('account/login/', views.user_login, name='user-login'),
    path('account/register/', views.user_register, name='user-register'),
    
    path('', views.homepage, name='homepage'),
]
