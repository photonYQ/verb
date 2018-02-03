# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics, permissions, status, mixins
from rest_framework.views import APIView
from rest_framework.response import Response

from blog import models, serializers


class PostList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

    def list(self, request, format=None):
        queryset = self.get_queryset()
        serializer = serializers.PostListSerializer(queryset, many=True)
        return Response(serializer.data)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class TagList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagListSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class CommentDetail(generics.RetrieveDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    

class BlogIngo(generics.CreateAPIView):
    queryset = models.BlogInfo.objects.all()
    serializer_class = serializers.BlogInfoSerializer
