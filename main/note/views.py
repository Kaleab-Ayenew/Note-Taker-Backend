from note.models import Note
from django.contrib.auth.models import User

#DRF Imports

from rest_framework.decorators import api_view
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.response import Response

from note.serializers import NoteSerializer, UserSerializer

api_view['GET','POST']
def note_list(request, format=None):

    if request.method == 'GET':

        notes = Note.objects.all()
        serializer = NoteSerializer(notes)

