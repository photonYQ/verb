# -*- coding:utf-8 -*-

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from blog import views


urlpatterns = [
    url(r'^posts/$', views.PostList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)