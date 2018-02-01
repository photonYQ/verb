# -*- coding:utf-8 -*-

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from blog import views


urlpatterns = [
    url(r'^posts/$', views.PostList.as_view()),
    url(r'^tags/$', views.TagList.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)$', views.PostDetail.as_view()),
    url(r'^tags/(?P<pk>[0-9]+)$', views.TagDetail.as_view()),
    url(r'^comments/$', views.CommentList.as_view()),
    url(r'^comments/(?P<pk>[0-9]+)$', views.CommentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)