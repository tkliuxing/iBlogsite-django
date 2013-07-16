#-*- coding: utf-8 -*-
from django.db import models
from django.db.models import Sum
from django.utils.translation import ugettext as _


class TouPiao(models.Model):
    title = models.CharField(_(u"标题"), max_length=50)
    description = models.TextField(_(u"描述"), default=_(u"暂无"))
    start_date = models.DateField(_(u"开始时间"))
    end_date = models.DateField(_(u"结束时间"))

    class Meta:
        verbose_name = _(u'投票')
        verbose_name_plural = _(u'投票')

    def __unicode__(self):
        return self.title


class TouPiaoXiang(models.Model):
    name = models.CharField(_(u"项目标题"), max_length=50)
    count = models.IntegerField(_(u"次数"), default=0)
    toupiao = models.ForeignKey(
        TouPiao, verbose_name=_(u'投票'), related_name='xiangmu')
    ip_address = models.IPAddressField(_(u"IP地址"), default="0.0.0.0")

    class Meta:
        verbose_name = _(u'投票项')
        verbose_name_plural = _(u'投票项')

    @property
    def percent(self):
        total = self.toupiao.xiangmu.all().aggregate(total=Sum('count'))['total']
        if total == 0:
            return 0
        return self.count * 100 / total

    def __unicode__(self):
        return self.name


class TouPiaoJiLu(models.Model):
    username = models.CharField(_(u"用户名"), max_length=50)
    ip_address = models.IPAddressField(_(u"IP地址"))
    toupiao = models.ForeignKey(
        TouPiao, verbose_name=_(u'投票'), related_name='canyuzhe')
    xiangmu = models.ForeignKey(
        TouPiaoXiang, verbose_name=_(u'投票项'), related_name='xuanzezhe')

    class Meta:
        verbose_name = _(u'投票记录')
        verbose_name_plural = _(u'投票记录')

    def __unicode__(self):
        return u":".join([self.toupiao.title, self.xiangmu.name, self.ip_address])
