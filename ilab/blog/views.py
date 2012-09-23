#-*- coding: utf-8 -*-
from django.utils import simplejson as json
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from iblog.blog.models import Blog, Discuss
from iblog.blog.forms import DiscussForm, UserDiscussForm


def blog(request, blog):
    C = {}
    blog = get_object_or_404(Blog, pk=blog)
    C['blog'] = blog
    if request.user.is_authenticated():
        instance = Discuss(
            blog=blog,
            user=request.user,
            name=request.user.username,
            email=request.user.email,
        )
        form_model = UserDiscussForm
    else:
        instance = Discuss(blog=blog)
        form_model = DiscussForm

    C['form'] = form_model(instance=instance)

    if request.method == 'POST':
        form = form_model(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
        else:
            C['form'] = form

    return render_to_response('blog.html', C, context_instance=RequestContext(request))


@login_required
def discuss_del(request, discuss):
    discuss = get_object_or_404(Discuss, pk=discuss)
    discuss.delete()
    return HttpResponse(json.dumps({'success': True}))
