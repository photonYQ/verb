# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from blog import models, serializers


class PostViewset(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = models.Post.objects.all()
        tag_id = self.request.query_params.get('tag_id', None)
        if tag_id is not None:
            queryset = queryset.filter(tags__id=tag_id)
        return queryset
    
    def get_serializer_class(self):
        if self.action == "list":
            return serializers.PostListSerializer
        else:
            return serializers.PostSerializer


class TagViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = models.Tag.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.TagListSerializer
        else:
            return serializers.TagSerializer


class CommentViewSet(ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def get_permissions(self):
        if self.action == "destroy":
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
    

class BlogInfo(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = models.BlogInfo.objects.all()
    serializer_class = serializers.BlogInfoSerializer
