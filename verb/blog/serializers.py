# -*- coding:utf-8 -*-

from rest_framework import serializers

from .models import Post, Tag, Comment, BlogInfo


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'create_time', 'update_time', 'summary', 'tags')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'description')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'nick_name', 'email', 'reply', 'post', 'followed')


class BlogInfoSerializer(serializers.ModelSerializer):
    class Meta:
        models = BlogInfo
        fields = ('id', 'title', 'tip')