#DRF Imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#DJANGO IMPORTS
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect

#Application imports
from accounts.serializers import UserSerializer

api_view(['POST'])
def sign_up(request):

    user_data = request.data
    serializer = UserSerializer(user_data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    


