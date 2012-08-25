#-*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django_markdown.widgets import MarkdownWidget
from .models import Blog, Discuss


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    list_filter = ('user',)
    search_fields = ('title', 'content', 'user',)
    formfield_overrides = {models.TextField: {'widget': MarkdownWidget}}
admin.site.register(Blog, BlogAdmin)


class DiscussAdmin(admin.ModelAdmin):
    list_display = ('blog', 'user')
    list_filter = ('name',)
    search_fields = ('blog', 'name', 'user',)
    formfield_overrides = {models.TextField: {'widget': MarkdownWidget}}
admin.site.register(Discuss, DiscussAdmin)
