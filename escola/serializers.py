from rest_framework import serializers

from escola.models import Escola


class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = ['id','nome','endereco','estado','telefone','email','senha']