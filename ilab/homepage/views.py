#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from ilab.blog.models import Blog


def homepage(request):
    C = {}
    blogs = Blog.objects.all()
    C['blogs'] = blogs
    return render_to_response('index.html', C, context_instance=RequestContext(request))
