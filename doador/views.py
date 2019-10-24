from django.shortcuts import render
from rest_framework.decorators import action

# Create your views here.
from rest_framework import viewsets
from doacao.models import Doacao
from rest_framework.response import Response
from doacao.serializers import DoacaoSerializer

from doador.models import Doador
from doador.serializers import DoadorSerializer


class DoadorViewSet(viewsets.ModelViewSet):
    queryset = Doador.objects.all()
    serializer_class = DoadorSerializer

    @action(detail=True,methods=["GET"])
    def itensCadastrados(self,request,pk=None):
        doacao = Doacao.objects.all().filter(doador=pk)
        return Response(DoacaoSerializer(doacao, many=True).data) 