from rest_framework import serializers
from .models import TodoTask, User
from django.contrib.auth.password_validation import validate_password
#from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

class TodoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=TodoTask
        fields= "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']

        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError('A user with this email and password is not found.')
        try:
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError('User with given email and password does not exists')
        return {
            'email':user.email,

        }