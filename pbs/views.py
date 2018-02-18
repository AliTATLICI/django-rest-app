from django.shortcuts import render

from rest_framework import viewsets
from pbs.models import Birim
from pbs.serializers import BirimSerializer

class BirimViewSet(viewsets.ModelViewSet):
    queryset = Birim.objects.all()
    serializer_class = BirimSerializer

# Create your views here.
