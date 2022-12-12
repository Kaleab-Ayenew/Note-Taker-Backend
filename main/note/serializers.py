from rest_framework import serializers
from note.models import Note

class NoteSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Note
        fields = '__all__'