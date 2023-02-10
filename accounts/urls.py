from django.urls import path
from . import views 

urlpatterns = [
    path('', views.registerUser, name="registerPage"),
    path('loginPage/', views.loginPage, name="loginPage"),
    path('profile/', views.profile, name="profile")
]
