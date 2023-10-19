from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Review

User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'location')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            location=validated_data['location']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'restaurant_id', 'user', 'rating', 'text', 'date']
        read_only_fields = ('date', 'user')

class UserSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'location', 'reviews']