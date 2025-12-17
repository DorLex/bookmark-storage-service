from logging import Logger, getLogger

from rest_framework.generics import get_object_or_404
from rest_framework.utils.serializer_helpers import ReturnDict

from accounts.models import User
from bookmarks.models import Bookmark
from bookmarks.serializers.bookmark import BookmarkInputSerializer, BookmarkSerializer
from og_parser.parser import OgParser

logger: Logger = getLogger(__name__)


class BookmarkService:
    def create_bookmark(self, user: User, bookmark_data: dict) -> ReturnDict:
        input_serializer: BookmarkInputSerializer = BookmarkInputSerializer(data=bookmark_data)
        input_serializer.is_valid(raise_exception=True)

        url: str = input_serializer.data['url']
        og_parser: OgParser = OgParser(url)

        data: dict = {
            'user': user.pk,
            'title': og_parser.title,
            'description': og_parser.description,
            'url': url,
            'url_type': og_parser.type,
            'image': og_parser.image,
        }

        serializer: BookmarkSerializer = BookmarkSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # TODO: настроить Джанго логи
        logger.info(f'Сохранена ссылка: {url=}, {user.pk=}')

        return serializer.data

    def get_bookmark(self, user: User, bookmark_id: int) -> ReturnDict:
        bookmark: Bookmark = get_object_or_404(Bookmark, user=user, pk=bookmark_id)
        serializer: BookmarkSerializer = BookmarkSerializer(bookmark)
        return serializer.data

    def update_bookmark(
        self,
        user: User,
        bookmark_id: int,
        bookmark_data: dict,
        *,
        partial: bool,
    ) -> ReturnDict:
        bookmark: Bookmark = get_object_or_404(Bookmark, user=user, pk=bookmark_id)
        serializer: BookmarkSerializer = BookmarkSerializer(bookmark, bookmark_data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    def delete_bookmark(self, user: User, bookmark_id: int) -> ReturnDict:
        bookmark: Bookmark = get_object_or_404(Bookmark, user=user, pk=bookmark_id)
        bookmark.delete()
        serializer: BookmarkSerializer = BookmarkSerializer(bookmark)
        return serializer.data
