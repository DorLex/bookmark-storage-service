from rest_framework import serializers


class UrlSerializer(serializers.Serializer):
    url = serializers.URLField()


class IDSerializer(serializers.Serializer):
    id = serializers.IntegerField()
