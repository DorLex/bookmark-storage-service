from rest_framework import serializers

from .models import Collections


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collections
        fields = '__all__'


class CollectionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collections
        fields = ('title', 'description')
