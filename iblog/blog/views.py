#-*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from iblog.blog.models import Blog, Discuss
from iblog.blog.forms import DiscussForm, UserDiscussForm, BlogForm, BlogEditForm


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

    return render(request, 'blog.html', C)


@login_required
def write(request):
    """Write Blog view."""
    C = {}
    C['form'] = BlogForm(instance=Blog(user=request.user))
    if request.method == "POST":
        form = BlogForm(data=request.POST, instance=Blog(user=request.user))
        if form.is_valid():
            tags = form.cleaned_data['tags']
            blog = form.save()
            blog.tags.reconstruct(blog, tags)
            blog.tags.update(frozen=True)
            return redirect(blog.get_absolute_url())
        C['form'] = form
    return render(request, 'write.html', C)


@login_required
def edit(request, blog_id):
    """Write Blog view."""
    C = {}
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.user = request.user
    C['form'] = BlogEditForm(instance=blog)
    if request.method == "POST":
        form = BlogEditForm(data=request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect(blog.get_absolute_url())
        C['form'] = form
    return render(request, 'write.html', C)


@login_required
def discuss_del(request, discuss):
    discuss = get_object_or_404(Discuss, pk=discuss)
    discuss.delete()
    return HttpResponse(json.dumps({'success': True}))
