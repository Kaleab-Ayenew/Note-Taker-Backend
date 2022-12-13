from rest_framework import serializers
from django.contrib.auth.models import User
from note.models import Note

class UserSerializer(serializers.ModelSerializer):
    notes = serializers.RelatedField(many=True, queryset= Note.objects.all())
    class Meta:
        fields = ['id', 'username', 'notes']
        model = User