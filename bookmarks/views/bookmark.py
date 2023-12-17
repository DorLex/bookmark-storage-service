from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from bookmarks.models import Bookmark
from bookmarks.serializers import BookmarkSerializer


class BookmarkAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, bookmark_id):
        """Получить закладку"""

        bookmark = get_object_or_404(Bookmark, user=request.user, pk=bookmark_id)
        serializer = BookmarkSerializer(bookmark)

        return Response(serializer.data)

    def delete(self, request, bookmark_id):
        """Удалить закладку"""

        bookmark = get_object_or_404(Bookmark, user=request.user, pk=bookmark_id)
        bookmark.delete()

        serializer = BookmarkSerializer(bookmark)

        return Response(serializer.data, status.HTTP_204_NO_CONTENT)
