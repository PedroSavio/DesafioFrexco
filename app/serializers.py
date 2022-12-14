from rest_framework import serializers
from app.models.models import Usuario

class UsuarioSerializer (serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('login', 'senha', 'dataNascimento')