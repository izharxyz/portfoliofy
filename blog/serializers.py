from rest_framework import serializers

from .models import Category, Post, PostContent


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug", "description", "image", "posts_count"]


class PostContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostContent
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "slug", "categories", "description",
                  "image", "featured", "reading_time", "created_at", "updated_at"]


class PostDetailSerializer(PostSerializer):
    content = PostContentSerializer(many=True, read_only=True)

    class Meta(PostSerializer.Meta):
        fields = PostSerializer.Meta.fields + ["content"]
