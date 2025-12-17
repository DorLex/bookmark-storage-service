from django.contrib.auth import get_user_model
from rest_framework import serializers

from accounts.models import User as UserModel

User: type[UserModel] = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model: type[UserModel] = User
        fields: tuple = ('email', 'password')
        extra_kwargs: dict = {'password': {'write_only': True}}

    def create(self, validated_data: dict) -> User:
        user: User = User.objects.create_user(**validated_data)
        return user
