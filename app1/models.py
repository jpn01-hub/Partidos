from django.db import models
from rest_framework import serializers

class Partido(models.Model):
    Codigo = models.IntegerField()
    Nombre = models.CharField(max_length=50)
    Sigla = models.CharField(max_length=10)

class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = ["Codigo","Nombre", "Sigla"]