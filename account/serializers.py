from rest_framework import serializers
from .models import *
# from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email','name' ,'password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError(
                "Password and Confirm Password doesn't match")
        return attrs

    def create(self, validate_data):
        password2 = validate_data.pop('password2', None)
        return User.objects.create_user(**validate_data)

    # # another way to create user manually
    # def create(self, validated_data):
    #     # Retrieve the password from the validated_data dictionary
    #     password = validated_data.pop('password2', None)
    #     password = validated_data.pop('password', None)
    #     # Create a new User instance with the remaining validated_data
    #     user = User.objects.create(**validated_data)
    #     # Set the password for the user instance
    #     if password:
    #         user.set_password(password)
    #     # Save the user instance to the database
    #     user.save()

    #     return user
