from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="home"),
    path('profile/', views.profile, name="profil"),
    path('enregisterement/', views.register, name='register'),
    path('addSchool/', views.registerSchool, name='addSchool'),
    path('addClass/', views.registerClass, name="addClass"),
    path('listEtudiant/', views.ListStudent, name='listeE'),
    path('modifier/<int:id>/', views.modifier,name="modifierE"),
    path('supprimer/<int:id>/', views.delete,name="supprimerE"),
    path('registerP/', views.registerProfil,name="registerP"),
    path('login/', views.connexion,name="login"),
    path('logout/', views.deconnexion,name="logout"),







]
