## Import de bibliotecas Django e Rest Framework
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

## Import de bibliotecas basicas do Python
from random import choice

#Models, Serializers, Utils
from app.models.models import Usuario
from app.serializers import UsuarioSerializer

# Import da função que gera uma senha aleatório
from app.utils.SenhaAleatoria import RandomPassword


# Funções Controllers
## Função para CADASTRAR um usuário
@csrf_exempt
def Create(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)

        # Verifica se existe senha, caso não exista, gera uma senha aleatória
        if user_data["senha"] == "":
            user_data["senha"] = RandomPassword()

        # Serializa os dados recebidos
        user_serializer = UsuarioSerializer(data=user_data)

        # Verifica se o usuário é valido
        if user_serializer.is_valid():
            print("User Serializer", user_serializer)
            user_serializer.save()
            return JsonResponse("Usuario adicionado com sucesso!", safe=False)
        return JsonResponse("Usuario invalido!", safe=False)
    else:
        return JsonResponse("ERRO 500: metodo nao permitido!", safe=False)

## Função para Consultar todos os usuários em formato JSON
@csrf_exempt
def Index(request):
        if request.method == 'GET':
            users = Usuario.objects.all()
            users_serializer = UsuarioSerializer(users, many=True)
            return JsonResponse(users_serializer.data, safe=False)
        else:
            return JsonResponse("ERRO 500: metodo não permitido!", safe=False)


