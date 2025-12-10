from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from bookmarks.models import Bookmark
from bookmarks.serializers.bookmark import BookmarkInputSerializer, BookmarkSerializer
from og_parser.parser import Parser
from og_parser.request_utils import get_page_html


@extend_schema(tags=['Bookmarks'])
class BookmarkViewSet(ViewSet):
    permission_classes: tuple = (IsAuthenticated,)

    @extend_schema(
        request=BookmarkInputSerializer,
        responses=BookmarkSerializer,
    )
    def create(self, request: Request) -> Response[dict]:
        """Добавить ссылку."""
        input_serializer: BookmarkInputSerializer = BookmarkInputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        url: str = input_serializer.data.get('url')

        page_html: str = get_page_html(url)
        parser: Parser = Parser(page_html)

        data: dict = {
            'user': request.user.id,
            'title': parser.title,
            'description': parser.description,
            'url': url,
            'url_type': parser.type,
            'image': parser.image,
        }

        serializer: BookmarkSerializer = BookmarkSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    @extend_schema(responses=BookmarkSerializer)
    def retrieve(self, request: Request, bookmark_id: int) -> Response[dict]:
        """Получить ссылку."""
        bookmark: Bookmark = get_object_or_404(Bookmark, user=request.user, pk=bookmark_id)
        serializer: BookmarkSerializer = BookmarkSerializer(bookmark)
        return Response(serializer.data)

    @extend_schema(
        request=BookmarkSerializer,
        responses=BookmarkSerializer,
    )
    def partial_update(self, request: Request, bookmark_id: int) -> Response[dict]:
        """Обновить ссылку частично."""
        bookmark: Bookmark = get_object_or_404(Bookmark, user=request.user, pk=bookmark_id)
        serializer: BookmarkSerializer = BookmarkSerializer(bookmark, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    @extend_schema(responses={status.HTTP_200_OK: BookmarkSerializer})
    def destroy(self, request: Request, bookmark_id: int) -> Response[dict]:
        """Удалить ссылку."""
        bookmark: Bookmark = get_object_or_404(Bookmark, user=request.user, pk=bookmark_id)
        bookmark.delete()
        serializer: BookmarkSerializer = BookmarkSerializer(bookmark)

        return Response(serializer.data, status.HTTP_200_OK)
