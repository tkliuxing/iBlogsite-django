#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator
from ilab.blog.models import Blog


def homepage(request):
    C = {}
    blogs = Blog.objects.all()
    p = Paginator(blogs, 10)
    try:
        page = p.page(int(request.GET.get('p', 1)))
    except:
        page = p.page(1)
    C['blogs'] = page.object_list
    C['pagination'] = page
    C['request'] = request
    return render_to_response('index.html', C, context_instance=RequestContext(request))
