#DRF Imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#DJANGO IMPORTS
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404, get_list_or_404

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

@api_view(['POST'])
def login_view(request):

    login_data = request.data

    user_name = request.data['username']
    password = request.data['password']

    user_instance = authenticate(request, username=user_name, password=password)
    if user_instance is not None:
        login(request, user_instance)
        login_data = request.data
        login_data['status'] = "ok"
        return Response(login_data, status=status.HTTP_200_OK)
    else:
        login_data = {"status":"failed"}
        return Response(login_data, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def logout_view(request):
    logout(request)
    logout_status = {"status":"ok"}
    return Response(logout_status, status=status.HTTP_200_OK)

@api_view(['GET','PUT', 'DELETE'])
def user_actions(request, username):
    user_instance = get_object_or_404(User, username=username)

    if request.method == "GET":
        serializer = UserSerializer(user_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = UserSerializer(user_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        user_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





    


