# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
    """docstring for Article."""

    title=models.CharField(max_length=100)#文章题目
    category=models.CharField(max_length=50,blank=True)#部门
    date_time=models.DateTimeField(auto_now_add=True)#发布日期
    content=models.TextField(blank=True,null=True)#文章正文

    def __unicode__(self):
        return self.title

    class Meta:
        ordering=['-date_time']
