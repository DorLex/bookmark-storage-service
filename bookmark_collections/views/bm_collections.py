from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from bookmark_collections.serializers import CollectionSerializer


class CollectionsAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """Добавить коллекцию"""

        request.data['user'] = request.user.id

        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
