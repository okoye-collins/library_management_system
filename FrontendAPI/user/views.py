from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, CreateAPIView

from user.models import User
from .serializers import UserSignupSerializer

# Create your views here.


class UserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
