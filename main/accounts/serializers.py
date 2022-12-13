from rest_framework import serializers
from django.contrib.auth.models import User
from note.models import Note

class UserSerializer(serializers.ModelSerializer):
    # notes = serializers.RelatedField(many=True, queryset= Note.objects.all())
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        new_user_name = validated_data['username']
        new_password = validated_data['password']
        new_email = validated_data['email']

        new_user = User.objects.create_user(username=new_user_name, password=new_password, email=new_email)
        return new_user

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.set_password(validated_data['password'])
        instance.email = validated_data['email']
        instance.save()
        return instance

    class Meta:
        fields = ['id', 'username', 'password', 'email', 'notes']
        model = User