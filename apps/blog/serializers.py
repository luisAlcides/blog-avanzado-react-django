from rest_framework import serializers
from .models import Post
from apps.category.serializers import CategorySerializer


class PostSerializer(serializers.ModelSerializer):
    thumbnail = serializers.CharField(source='get_thumbnail')
    video = serializers.CharField(source='get_video')
    class Meta:
        model = Post
        category = CategorySerializer()
        fields = [
            'blog_uuid',
            'title',
            'slug',
            'thumbnail',
            'video',
            'description',
            'excerpt',
            'category'
            'published',
            'status'
            'author',
        ]