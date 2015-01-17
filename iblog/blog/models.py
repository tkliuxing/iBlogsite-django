#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from universaltag.fields import UniversalTagField


class Blog(models.Model):
    user = models.ForeignKey('auth.User', verbose_name=_('作者'))
    title = models.CharField(max_length=30, null=False, blank=False, verbose_name=_('标题'))
    content = models.TextField(null=False, blank=False, verbose_name=_('内容'))
    tags = UniversalTagField()
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=_('创建时间'))
    edit_time = models.DateTimeField(auto_now=True, verbose_name=_('修改时间'))

    class Meta:
        verbose_name = _('文章')
        verbose_name_plural = _('文章')

    def __unicode__(self):
        return u"%s : %s %s" % (self.user.get_full_name(), self.edit_time.strftime("%Y-%m-%d %H:%M"), self.title)

    def get_absolute_url(self):
        return reverse('blog', args=[self.pk])


class Discuss(models.Model):
    user = models.ForeignKey('auth.User', verbose_name=_('评论用户'), null=True)
    blog = models.ForeignKey(Blog, verbose_name='Blog', related_name='discuess')
    name = models.CharField(max_length=200, verbose_name=_('昵称'), null=True, blank=True)
    email = models.EmailField(db_index=True, verbose_name=_('邮件地址'), null=True, blank=True)
    content = models.TextField(max_length=2000, verbose_name=_('内容'), null=False, blank=False)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=_('创建时间'))

    class Meta:
        verbose_name = _('文章评论')
        verbose_name_plural = _('文章评论')

    def __unicode__(self):
        if self.user:
            return u"%s @ %s" % (self.user, self.create_time)
        else:
            return u"%s @ %s" % (self.email, self.create_time)
