from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        obj = User.objects.create(**validated_data)
        return obj
    