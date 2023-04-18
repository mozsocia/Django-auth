from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        # Retrieve the password from the validated_data dictionary
        password = validated_data.pop('password', None)
        # Create a new User instance with the remaining validated_data
        user = User.objects.create(**validated_data)
        # Set the password for the user instance
        if password:
            user.set_password(password)
        # Save the user instance to the database
        user.save()

        return user
