from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from escola.models import Escola
from escola.serializers import EscolaSerializer


class EscolaViewSet(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer
