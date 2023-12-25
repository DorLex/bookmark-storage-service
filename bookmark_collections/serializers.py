from rest_framework import serializers

from .models import Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


class CollectionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('title', 'description')
