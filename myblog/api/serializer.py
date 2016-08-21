from rest_framework import serializers
from blog.models import *


class PostsSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=200)
    content = serializers.CharField(required=False, allow_blank=True, max_length=200)
    created_at = serializers.DateField()
    published_at = serializers.DateField()


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Post.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.code)
        instance.created_at = validated_data.get('created_at', instance.code)
        instance.published_at = validated_data.get('published_at', instance.code)
        instance.save()
        return instance
