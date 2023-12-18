from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from bookmark_collections.models import Collections
from bookmark_collections.serializers import CollectionSerializer, CollectionUpdateSerializer


class CollectionAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, collection_id):
        """Получить коллекцию"""

        collection = get_object_or_404(Collections, user=request.user, pk=collection_id)
        serializer = CollectionSerializer(collection)

        return Response(serializer.data)

    def patch(self, request, collection_id):
        """Частично обновить коллекцию"""

        collection = get_object_or_404(Collections, user=request.user, pk=collection_id)

        serializer = CollectionUpdateSerializer(collection, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, collection_id):
        """Удалить коллекцию"""

        collection = get_object_or_404(Collections, user=request.user, pk=collection_id)
        collection.delete()

        serializer = CollectionSerializer(collection)

        return Response(serializer.data, status.HTTP_204_NO_CONTENT)
