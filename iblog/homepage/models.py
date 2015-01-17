#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext as _


class UserProfile(models.Model):
    GENDER_CHOICES = (
        (0, _('女')),
        (1, _('男')),
        (2, _('保密')),
    )
    user = models.OneToOneField('auth.User')
    gender = models.IntegerField(default=2, choices=GENDER_CHOICES, verbose_name=_('性别'))
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name=_('简介'))
    show_in_page = models.BooleanField(default=False, verbose_name=_('显示在页面中'))

    class Meta:
        verbose_name = _('用户详情')
        verbose_name_plural = _('用户详情')

    def __unicode__(self):
        return self.user.username
