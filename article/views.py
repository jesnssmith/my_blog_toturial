# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from models import Article
# Create your views here.
def home(request):
    post_list=Article.objects.all()
    return render(request,'article/home.html',{'post_list':post_list})


def detail(request,my_args):
    return HttpResponse("You're looking at my_args %s." %my_args)

def test(request):
    return render(request,'article/test.html',{'current_time':datetime.now()})
