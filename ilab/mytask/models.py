#-*- coding: utf-8 -*-
from django.db import models
from json_field import JSONField


class MyTask(models.Model):
    """
    经纪人任务模型
    根据不同任务的不同逻辑需求修改config字典中的相关数据
    """
    user = models.OneToOneField('auth.User')
    config = JSONField(null=True)


class AgencyTask(object):
    def __init__(self, user):
        self.user = user
        self.config = MyTask.objects.get(user=user).config

    @property
    def weight(self):
        return self.task_weight

    @property
    def is_done(self):
        """
        判断任务是否已完成,根据不同任务的不同逻辑来判断
        返回True/False
        需重写
        """
        assert ValueError("Not define is_done method!")

    @property
    def alert_text(self):
        """
        任务提示文字,返回任务未完成时的文字提示信息
        返回字符串
        需重写
        """
        return self.task_alert_text

    @property
    def comment_text(self):
        """
        任务提示文字后的注释信息.
        """
        return self.task_comment_text

    @property
    def done_text(self):
        """
        任务完成后的文字信息.
        """
        return self.task_done_text

    @property
    def button_text(self):
        """
        任务链接按钮的文字信息.
        """
        return self.task_button_text

    @property
    def button_url(self):
        """
        任务链接按钮的链接地址.
        """
        return self.task_button_url
