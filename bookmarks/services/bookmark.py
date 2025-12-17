from rest_framework.utils.serializer_helpers import ReturnDict

from bookmarks.serializers.bookmark import BookmarkInputSerializer, BookmarkSerializer
from og_parser.parser import OgParser


class BookmarkService:
    def create_bookmark(self, user_id: int, bookmark_data: dict) -> ReturnDict:
        input_serializer: BookmarkInputSerializer = BookmarkInputSerializer(data=bookmark_data)
        input_serializer.is_valid(raise_exception=True)

        url: str = input_serializer.data['url']
        og_parser: OgParser = OgParser(url)

        data: dict = {
            'user': user_id,
            'title': og_parser.title,
            'description': og_parser.description,
            'url': url,
            'url_type': og_parser.type,
            'image': og_parser.image,
        }

        serializer: BookmarkSerializer = BookmarkSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data
