from rest_framework import serializers

from .models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'


class LinkSerializer(serializers.Serializer):
    link = serializers.URLField()


class IDSerializer(serializers.Serializer):
    id = serializers.IntegerField()
