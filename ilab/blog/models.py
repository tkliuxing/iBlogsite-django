#-*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from universaltag.fields import UniversalTagField


class Blog(models.Model):
    user = models.ForeignKey('auth.User', verbose_name=_(u'作者'))
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


class Discuss(models.Model):
    user = models.ForeignKey('auth.User', verbose_name=_(u'评论用户'), null=True)
    blog = models.ForeignKey(Blog, verbose_name=u'Blog', related_name='discuess')
    name = models.CharField(max_length=200, verbose_name=_(u'昵称'), null=True, blank=True)
    email = models.EmailField(db_index=True, verbose_name=_(u'邮件地址'), null=True, blank=True)
    content = models.TextField(max_length=2000, verbose_name=_(u'内容'), null=False, blank=False)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=_(u'创建时间'))

    class Meta:
        verbose_name = _(u'文章评论')

    def __unicode__(self):
        if self.user:
            return u"%s @ %s" % (self.user, self.create_time)
        else:
            return u"%s @ %s" % (self.email, self.create_time)
