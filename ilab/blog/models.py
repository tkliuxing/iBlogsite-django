#-*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from universaltag.fields import UniversalTagField


class Blog(models.Model):
    user = models.ForeignKey('auth.USER', verbose_name=_(u'作者'))
    title = models.CharField(max_length=30, null=False, blank=False, verbose_name=_(u'标题'))
    content = models.TextField(null=False, blank=False, verbose_name=_(u'内容'))
    tags = UniversalTagField()
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=_(u'创建时间'))
    edit_time = models.DateTimeField(auto_now=True, verbose_name=_(u'修改时间'))

    class Meta:
        verbose_name = _(u'Blog')
        verbose_name_plural = _(u'Blogs')

    def __unicode__(self):
        return u"%s : %s" % (self.user, self.title)
