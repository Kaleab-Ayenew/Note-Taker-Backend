from rest_framework import serializers
from note.models import Note
from django.contrib.auth.models import User

class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model = Note
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    notes = serializers.RelatedField(many=True, queryset= Note.objects.all(), read_only=True)
    class Meta:
        fields = "__all__"
        model = User

# class NoteSerializer(serializers.HyperlinkedModelSerializer):
#     owner = serializers.ReadOnlyField(source="owner.username")
#     class Meta:
#         model = Note
#         fields = '__all__'

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     notes = serializers.HyperlinkedRelatedField(many=True, view_name='note-content', read_only=True)
#     class Meta:
#         fields = "__all__"
#         model = User