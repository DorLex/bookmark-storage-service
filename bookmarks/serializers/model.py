from rest_framework import serializers

from bookmarks.models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model: type[Bookmark] = Bookmark
        fields: tuple | str = '__all__'
