#DRF Imports
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

#DJANGO IMPORTS
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt

#Application imports
from accounts.serializers import UserSerializer


@api_view(['POST'])
@permission_classes((AllowAny,))
def signup_view(request):

    user_data = request.data
    serializer = UserSerializer(data=user_data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def login_view(request):
    if request.user.is_authenticated:
        print("The User is Already Authenticated")
        return Response({"error":"You are already logged in"})
        
    login_data = request.data

    user_name = request.data.get('username')
    password = request.data.get('password')

    if user_name is None or password is None:
        error = {"error":"please provide both username and password"}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
    
    user_instance = authenticate(request, username=user_name, password=password)

    if user_instance is not None:
        token, _ = Token.objects.get_or_create(user=user_instance)
        login_data = {}
        login_data['username'] = request.data['username']
        login_data['status'] = "ok"
        login_data['token'] = token.key
        return Response(login_data, status=status.HTTP_200_OK)
    else:
        error = {"error":"Please provide valid credentials"}
        return Response(error, status=status.HTTP_401_UNAUTHORIZED)


# @api_view(['POST'])
# def logout_view(request):
#     logout(request)
#     logout_status = {"status":"ok"}
#     return Response(logout_status, status=status.HTTP_200_OK)



@api_view(['GET','PUT', 'DELETE'])
def user_actions(request, username):
    user_instance = get_object_or_404(User, username=username)
    if request.user == user_instance:
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
        
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)

