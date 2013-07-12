#-*- coding: utf-8 -*-
from django.contrib import admin
from .models import TouPiao, TouPiaoJiLu, TouPiaoXiang


class TouPiaoJiLuAdmin(admin.ModelAdmin):
    list_display = ('toupiao', 'xiangmu', 'ip_address', 'username')
    search_fields = ('toupiao__title', 'ip_address', 'username')
admin.site.register(TouPiaoJiLu, TouPiaoJiLuAdmin)


class TouPiaoXiangAdmin(admin.ModelAdmin):
    list_display = ('toupiao', 'name', 'count')
    search_fields = ('toupiao__title', 'name')
admin.site.register(TouPiaoXiang, TouPiaoXiangAdmin)


class TouPiaoXiangInline(admin.TabularInline):
    model = TouPiaoXiang
    readonly_fields = ('count', )


class TouPiaoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'end_date')
    search_fields = ('title', 'description',)
    inlines = (TouPiaoXiangInline, )
admin.site.register(TouPiao, TouPiaoAdmin)
