from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import BookmarkSerializer


class BookmarkAPIView(APIView):
    def post(self, request):
        link = request.data.get('link')

        # делаем запрос по ссылке
        # парсим

        # serializer = BookmarkSerializer(data=data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()

        return Response({}, status.HTTP_201_CREATED)
