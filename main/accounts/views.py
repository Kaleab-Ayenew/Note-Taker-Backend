#DRF Imports
from rest_framework.decorators import api_view
from rest_framework.response import Response


#DJANGO IMPORTS
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect

api_view(['POST'])
def sign_up(request):

    user_data = request.data
    new_user_name = user_data['username']
    new_password = user_data['password']
    
