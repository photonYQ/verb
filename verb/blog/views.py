# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework import permissions

from .models import Post, Tag, Comment, BlogInfo
from .serializers import PostSerializer, TagSerializer, CommentSerializer, BlogInfoSerializer


class PostList(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TagList(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CommentList(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class BlogIngo(CreateAPIView):
    queryset = BlogInfo.objects.all()
    serializer_class = BlogInfoSerializer

