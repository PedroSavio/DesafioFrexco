from django.db import models
# Create your models here.
class Usuario (models.Model):
    login = models.CharField(max_length=25)
    senha = models.CharField(max_length=20)
    dataNascimento = models.DateField()