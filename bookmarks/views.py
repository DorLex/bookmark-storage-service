from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from bookmarks.serializers import BookmarkSerializer
from og_parser.parser import Parser
from og_parser.request_utils import get_page_html


class BookmarkAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        link = request.data.get('link')

        page_html = get_page_html(link)
        parser = Parser(page_html)

        data = {
            'user': request.user.id,
            'title': parser.title,
            'description': parser.description,
            'url': link,
            'url_type': parser.type,
            'image': parser.image
        }

        serializer = BookmarkSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
