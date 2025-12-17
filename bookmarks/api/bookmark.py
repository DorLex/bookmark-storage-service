from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework.viewsets import ViewSet

from bookmarks.serializers.bookmark import BookmarkInputSerializer, BookmarkSerializer
from bookmarks.services.bookmark import BookmarkService


@extend_schema(tags=['Bookmarks'])
class BookmarkViewSet(ViewSet):
    permission_classes: tuple = (IsAuthenticated,)

    @extend_schema(
        request=BookmarkInputSerializer,
        responses=BookmarkSerializer,
    )
    def create(self, request: Request) -> Response[dict]:
        """Добавить ссылку."""
        bookmark_service: BookmarkService = BookmarkService()
        bookmark: ReturnDict = bookmark_service.create_bookmark(request.user, request.data)
        return Response(bookmark, status.HTTP_201_CREATED)

    @extend_schema(responses=BookmarkSerializer)
    def retrieve(self, request: Request, bookmark_id: int) -> Response[dict]:
        """Получить ссылку."""
        bookmark_service: BookmarkService = BookmarkService()
        bookmark: ReturnDict = bookmark_service.get_bookmark(request.user, bookmark_id)
        return Response(bookmark)

    @extend_schema(
        request=BookmarkSerializer,
        responses=BookmarkSerializer,
    )
    def partial_update(self, request: Request, bookmark_id: int) -> Response[dict]:
        """Обновить ссылку частично."""
        bookmark_service: BookmarkService = BookmarkService()
        bookmark: ReturnDict = bookmark_service.update_bookmark(request.user, bookmark_id, request.data, partial=True)
        return Response(bookmark)

    @extend_schema(responses={status.HTTP_200_OK: BookmarkSerializer})
    def destroy(self, request: Request, bookmark_id: int) -> Response[dict]:
        """Удалить ссылку."""
        bookmark_service: BookmarkService = BookmarkService()
        deleted_bookmark: ReturnDict = bookmark_service.delete_bookmark(request.user, bookmark_id)
        return Response(deleted_bookmark, status.HTTP_200_OK)
