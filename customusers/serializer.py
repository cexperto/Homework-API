from rest_framework import serializers
from rest_framework.validators import UniqueValidator, ValidationError
from django.contrib.auth.password_validation import validate_password

from customusers.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all(), message="Email is already used")]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])


    class Meta:
        model = CustomUser
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

    


