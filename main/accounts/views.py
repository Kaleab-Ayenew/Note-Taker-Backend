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

@api_view(['POST'])
def signup_view(request):

    user_data = request.data
    serializer = UserSerializer(data=user_data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view
def login_view(request):

    login_data = request.data
    serializer = UserSerializer(data=login_data)

    if serializer.is_valid():
        user_name = serializer.data['username']
        password = serializer.data['password']

        user_instance = authenticate(request, username=user_name, password=password)
        if user_instance is not None:
            login(request, user_instance)
            login_status = {"status":"ok"}
            return Response(login_status, status=status.HTTP_202_ACCEPTED)
        else:
            login_status = {"status":"failed"}
            return Response(login_status, status=status.HTTP_401_UNAUTHORIZED)



    


