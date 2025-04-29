from attrs import field
from rest_framework.serializers import ModelSerializer

from core.models import Modelo

class ModeloSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        field = "__all__"