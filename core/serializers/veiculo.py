from attrs import field
from rest_framework.serializers import ModelSerializer

from core.models import Veiculo

class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        field = "__all__"