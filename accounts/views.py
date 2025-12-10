from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from accounts.serializers import UserSerializer


class UserViewSet(ViewSet):
    @extend_schema(
        request=UserSerializer,
        responses=UserSerializer,
    )
    def create(self, request: Request) -> Response[dict]:
        """Регистрация пользователя."""
        serializer: UserSerializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
