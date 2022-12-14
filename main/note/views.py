from note.models import Note
from django.contrib.auth.models import User
from django.shortcuts import redirect

#DRF Imports

from rest_framework.decorators import api_view
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes

from note.serializers import NoteSerializer
from note.permissions import OwnsThisObject

@api_view(['GET','POST'])
def note_list(request, format=None):

    if request.method == 'GET':

        notes = Note.objects.filter(owner=request.user)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':

        data = request.data.dict()
        request_user_id = request.user.id
        data['owner'] = request_user_id
        serializer = NoteSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def note_content(request, pk, format=None):

    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = NoteSerializer(note)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        data = request.data.dict()
        request_user_id = request.user.id
        data['owner'] = request_user_id
        serializer = NoteSerializer(note,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



