# -*- coding:utf-8 -*-

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from blog import views


router = DefaultRouter()

router.register(r'posts', views.PostViewset, base_name="posts")

router.register(r'tags', views.TagViewSet, base_name="tags")

router.register(r'comments', views.CommentViewSet, base_name="comments")

router.register(r'bloginfo', views.BlogInfo, base_name="blog_info")

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls'))
]