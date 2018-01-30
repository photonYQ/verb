# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)

    def __str__():
        return "%s" % self.name


class Post(models.Model):
    title = models.CharField(max_length=64)
    create_time = models.DateField(auto_now=False, auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    summary = models.TextField(max_length=576)
    content = models.TextField()
    num_views = models.IntegerField(default=0)

    tags = models.ManyToManyField(Tag)

    def __str__():
        return "%s" % self.title

    class Meta:
        ordering = ["create_time"]


class Comment(models.Model):
    content = models.TextField(max_length=576)
    timestamp = models.DateTimeField(auto_now_add=True)
    nick_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    reply = models.CharField(max_length=64, default="post")
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    followed = models.ForeignKey('self', related_name='follower', on_delete=models.CASCADE)

    def __str__():
        return "%s reply to %s" % (self.nick_name, self.reply)


class BlogInfo(models.Model):
    title = models.CharField(max_length=64)
    tip = models.CharField(max_length=128)

    
