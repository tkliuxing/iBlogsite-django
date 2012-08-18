#-*- coding: utf-8 -*-
from django.contrib import admin
from .models import MyTask


class MyTaskAdmin(admin.ModelAdmin):
    pass
admin.site.register(MyTask, MyTaskAdmin)
