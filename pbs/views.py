from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from . import models
from . import serializers


class Index(TemplateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Empty Page')

class Transaksi(generics.ListCreateAPIView):
    queryset = models.Transaksi.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.TransaksiSeraializer

    def perform_create(self, serializer):
        serializer.save(pemilik=self.request.user)


class TransaksiModifikasi(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Transaksi.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.TransaksiSeraializer

    def get_queryset(self):
        return models.Transaksi.objects.filter(pemilik=self.request.user)

    def get_object(self):
        return get_object_or_404(models.Transaksi, pk=self.kwargs['transaksi_id'])


class Register(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Generate token for useer
        token = Token.objects.create(user=user)

        return Response({'detail': 'User has been created with Token: ' + token.key})


class ChangePassword(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, username=request.user)
        user.set_password(request.POST.get('new_password'))
        user.save()

        return Response({'detail': 'Password has been saved.'})




class BirimViewSet(viewsets.ModelViewSet):
    queryset = models.Birim.objects.all()
    #permission_classes = (permissions.IsAuthenticated, )
    serializer_class = serializers.BirimSerializer

# Create your views here.
