#DRF Imports
from rest_framework.decorators import api_view
from rest_framework.response import Response


#DJANGO IMPORTS
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect

