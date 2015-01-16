#-*- coding: utf-8 -*-
import datetime
import urlparse
from django.utils.translation import ugettext as _
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator
from django.contrib.auth import REDIRECT_FIELD_NAME, logout as auth_logout
from iblog.blog.models import Blog


def homepage(request):
    C = {}
    blogs = Blog.objects.all().order_by('-create_time')
    p = Paginator(blogs, 10)
    try:
        page = p.page(int(request.GET.get('p', 1)))
    except:
        page = p.page(1)
    C['news'] = Blog.objects.filter(create_time__gt=datetime.datetime.now()+datetime.timedelta(days=-90))
    C['news'] = C['news'].order_by('-create_time')
    C['blogs'] = page.object_list
    C['pagination'] = page
    return render_to_response('index.html', C, context_instance=RequestContext(request))


def login(request):
    from django.contrib.auth.views import login as login_view
    from django.contrib.admin.forms import AdminAuthenticationForm
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    redirect_to = request.META.get("HTTP_REFERER", '/')
    if redirect_to:
        netloc = urlparse.urlparse(redirect_to)[1]
        # Security check -- don't allow redirection to a different host.
        if (netloc and netloc != request.get_host()):
            redirect_to = '/'
    context = {
        'title': _('Log in'),
        'app_path': request.get_full_path(),
        REDIRECT_FIELD_NAME: redirect_to,
    }
    defaults = {
        'extra_context': context,
        'authentication_form': AdminAuthenticationForm,
        'template_name': 'login.html',
    }
    return login_view(request, **defaults)


def logout(request):
    auth_logout(request)
    redirect_to = request.META.get("HTTP_REFERER", '')
    if redirect_to:
        netloc = urlparse.urlparse(redirect_to)[1]
        # Security check -- don't allow redirection to a different host.
        if not (netloc and netloc != request.get_host()):
            return HttpResponseRedirect(redirect_to)
    return HttpResponseRedirect('/')
