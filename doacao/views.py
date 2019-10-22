from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from doacao.models import Doacao
from doacao.serializers import DoacaoSerializer


class DoacaoViewSet(viewsets.ModelViewSet):
    queryset = Doacao.objects.all()
    serializer_class = DoacaoSerializer

    @action(detail=False,methods=['GET'])
    def disponiveis(self,request):
        doacao = Doacao.objects.all().filter(escola__isnull=True)
        return Response(DoacaoSerializer(doacao,many=True).data)
