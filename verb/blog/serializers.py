# -*- coding:utf-8 -*-

from rest_framework import serializers

from blog import models


class PostListSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)
    class Meta:
        model = models.Post
        fields = ('title', 'create_time', 'update_time', 'summary', 'num_views', 'num_comments', 'tags')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ('id', 'nick_name', 'email', 'reply', 'post', 'followed')


class PostSerializer(PostListSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = models.Post
        fields = PostListSerializer.Meta.fields + ('content', 'comments')


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = ('id', 'name', 'description', 'num_posts')


class TagSerializer(TagListSerializer):
    posts = PostListSerializer(many=True, read_only=True)
    class Meta:
        model = models.Tag
        fields = TagListSerializer.Meta.fields + ('posts', )


class BlogInfoSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.BlogInfo
        fields = ('id', 'title', 'tip')