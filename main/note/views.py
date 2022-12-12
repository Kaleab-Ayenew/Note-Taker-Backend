from note.models import Note
from django.contrib.auth.models import User

#DRF Imports

from rest_framework.decorators import api_view
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.response import Response
from rest_framework import status

from note.serializers import NoteSerializer, UserSerializer

api_view(['GET','POST'])
def note_list(request, format=None):

    if request.method == 'GET':

        notes = Note.objects.all()
        serializer = NoteSerializer(notes)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        
        data = request.data
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

api_view(['GET','PUT','DELETE'])
def note_content(request, pk, format=None):

    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)