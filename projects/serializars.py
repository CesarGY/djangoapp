from rest_framework import serializers
from .models import Project


# Notes: ModelViewSet
# Llamar un modelo especial de RestFramework
# Esto esta basado en un modelo creado anteriormente
# Desde aqui ProjectSerializer sabra que hacer cuando se llame POST GET PUT DELETE
# ViewSet determina quien va poder consultar un objeto
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at',)
