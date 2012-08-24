#-*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _


class UserProfile(models.Model):
    GENDER_CHOICES = (
        (0, _(u'女')),
        (1, _(u'男')),
        (2, _(u'保密')),
    )
    user = models.OneToOneField('auth.User')
    gender = models.IntegerField(default=2, choices=GENDER_CHOICES)
    description = models.TextField(max_length=2000, null=True, blank=True)

    class Meta:
        verbose_name = _('UserProfile')
        verbose_name_plural = _('UserProfiles')

    def __unicode__(self):
        return self.user.username
