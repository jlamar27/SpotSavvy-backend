from django.shortcuts import render

from rest_framework import viewsets
from .serializers import UserprofileSerializer, ReviewSerializer
from .models import Userprofile, Review

# Create your views here.

class UserprofileViewSet(viewsets.ModelViewSet):
    queryset = Userprofile.objects.all()
    serializer_class = UserprofileSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
