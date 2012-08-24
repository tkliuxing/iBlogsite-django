#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator
from ilab.blog.models import Blog


def blog(request, blog):
    C = {}
    blog = get_object_or_404(Blog, pk=blog)
    C['blog'] = blog
    return render_to_response('blog.html', C, context_instance=RequestContext(request))
