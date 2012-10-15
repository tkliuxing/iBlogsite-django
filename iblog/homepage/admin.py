#-*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender',)
    list_filter = ('user', 'gender',)
    search_fields = ('user', 'gender',)
admin.site.register(UserProfile, UserProfileAdmin)
