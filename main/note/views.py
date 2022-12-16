from note.models import Note
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

#DRF Imports

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from note.serializers import NoteSerializer


class NoteList(APIView):

    def get(self, request, format=None):

        user = request.user
        notes = Note.objects.filter(owner=user)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):

        try:
             data = request.data
             data['owner'] = request.user.id
        except AttributeError:
            data = request.data.dict()
            data['owner'] = request.user.id
    
        serializer = NoteSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteContent(APIView):

    def get_object(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        if request.user == note.owner:
            return note
        return None
        
    def get(self, request, pk, format=None):
        
        note = self.get_object(request, pk)
        if note is None:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = NoteSerializer(note)
        return Response(serializer.data)

    
    def put(self, request, pk, format=None):

        note = self.get_object(request, pk)
        if note is None:
            return Response(status=status.HTTP_403_FORBIDDEN)

        try:
             data = request.data
             data['owner'] = request.user.id
        except AttributeError:
            data = request.data.dict()
            data['owner'] = request.user.id
        
        serializer = NoteSerializer(note, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):

        note = self.get_object(request, pk)
        if note is None:
            return Response(status=status.HTTP_403_FORBIDDEN)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)