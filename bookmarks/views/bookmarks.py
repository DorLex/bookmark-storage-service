from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from bookmarks.serializers.data import UrlSerializer
from bookmarks.serializers.model import BookmarkSerializer
from og_parser.parser import Parser
from og_parser.request_utils import get_page_html


class BookmarksAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(request_body=UrlSerializer, responses={status.HTTP_201_CREATED: BookmarkSerializer()})
    def post(self, request):
        """Добавить закладку"""

        serializer = UrlSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        url = serializer.data.get('url')

        page_html = get_page_html(url)
        parser = Parser(page_html)

        data = {
            'user': request.user.id,
            'title': parser.title,
            'description': parser.description,
            'url': url,
            'url_type': parser.type,
            'image': parser.image
        }

        serializer = BookmarkSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
