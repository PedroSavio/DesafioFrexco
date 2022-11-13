from django.contrib import admin
from django.urls import path
from app.views import Index, Create

urlpatterns = [
    path('cadastro', Create),
    path('', Index),
]