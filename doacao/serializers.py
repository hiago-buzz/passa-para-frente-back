from rest_framework import serializers

from doacao.models import Doacao
from doador.models import Doador


class DoacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doacao
        fields = ['id','nome','doador','escola','descricao']