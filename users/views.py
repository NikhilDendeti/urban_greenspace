from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response  


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_details(request):
    user = request.user

    data = {
        'username': user.username,
        'email': user.email,
        'is_staff': user.is_staff
    }
    return JsonResponse(data, status=status.HTTP_200_OK)


@api_view(['POST'])
def register_user(request):
    User = get_user_model()
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    if not username or not password:
        return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists."}, status=status.HTTP_409_CONFLICT)

    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)