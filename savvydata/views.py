from django.shortcuts import render

from rest_framework import viewsets
from .serializers import UserSerializer, ReviewSerializer
from .models import User, Review

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
