from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from .serializers import UserSerializer, UserCreateSerializer, ReviewSerializer
from .models import Review
from rest_framework.exceptions import PermissionDenied

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
def signup_view(request):
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()

        # Authenticate the user and log them in.
        login(request, user)

        response_data = {
            "message": "User created successfully!",
            "user": UserSerializer(user).data,  # Include the serialized user data
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return Response({"message": "Logged in successfully!"})
    return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({"message": "Logged out successfully!"})

@api_view(['GET'])
def review_list(request, restaurant_id):
    """
    List all reviews for a specific restaurant.
    """
    reviews = Review.objects.filter(restaurant_id=restaurant_id).order_by('-date')
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request):
    """
    Create a new review.
    """
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_review(request, pk):
    """
    Update a review.
    """
    review = get_object_or_404(Review, pk=pk)
    if review.user != request.user:
        raise PermissionDenied("You do not have permission to edit this review.")
    serializer = ReviewSerializer(review, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_review(request, pk):
    """
    Delete a review.
    """
    review = get_object_or_404(Review, pk=pk)
    if review.user != request.user:
        raise PermissionDenied("You do not have permission to delete this review.")
    review.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)