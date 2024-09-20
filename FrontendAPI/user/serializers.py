from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User


class UserSignupSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255,  write_only=True)
    password2 = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]

    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Passwords must match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        validated_data['password'] = make_password(validated_data.pop('password1'))
        
        email = validated_data.get('email')
        username = email.split('@')[0]
        
        original_username = username
        counter = 1
        while User.objects.filter(username=username).exists():
            username = f"{original_username}{counter}"
            counter += 1
        
        validated_data['username'] = username
        
        user = User(**validated_data)
        user.save()
        return user