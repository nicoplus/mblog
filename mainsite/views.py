# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse

from models import Post


# Create your views here.

def homepage(request):
	posts = Post.objects.all()
	now = datetime.now()
	return render(request, 'index.html', locals())

def showpost(request, slug):
	post = Post.objects.get(slug = slug)
	if post:
		return render(request, 'post.html', locals())
	return redirect('/')


