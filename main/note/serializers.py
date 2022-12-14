from rest_framework import serializers
from note.models import Note
from django.contrib.auth.models import User

class NoteSerializer(serializers.ModelSerializer):
    owner_name = serializers.ReadOnlyField(source="owner.username")
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    class Meta:
        model = Note
        fields = '__all__'
        extra_kwargs = {'owner': {'write_only':True}}


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