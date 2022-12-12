from note.models import Note
from django.contrib.auth.models import User
from django.forms import 
#DRF Imports

from rest_framework.decorators import api_view
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.response import Response

api_view['GET','POST']
def note_list(request, format=None):

    if request.method ==
