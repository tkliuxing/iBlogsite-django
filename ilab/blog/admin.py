#-*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django_markdown.widgets import MarkdownWidget
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    list_filter = ('user',)
    search_fields = ('title', 'content', 'user',)
    formfield_overrides = {models.TextField: {'widget': MarkdownWidget}}
admin.site.register(Blog, BlogAdmin)
