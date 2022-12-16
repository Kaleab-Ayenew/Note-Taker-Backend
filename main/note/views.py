from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

#DRF Imports

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions

from note.serializers import NoteSerializer
from note.models import Note
from note.permissions import OwnsThisObject, IsAuthAndOwnsObject


class NoteList(generics.ListCreateAPIView):

    serializer_class = NoteSerializer

    def create(self, request, *args, **kwargs):
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

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

class NoteContent(generics.RetrieveUpdateDestroyAPIView):

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthAndOwnsObject] #Specifying a Permission Class List overides the default in the Setting

    def update(self, request, *args, **kwargs):
        try:
            data = request.data
            data['owner'] = request.user.id
        except AttributeError:
            data = request.data.dict()
            data['owner'] = request.user.id
        note = self.get_object() #You can get the Object of the View by calling this method
        serializer = NoteSerializer(note, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)