# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from blog import models, serializers


class PostList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostListSerializer

    def post(self, request, format=None):
        serializer = serializers.PostSerializer(datar=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
