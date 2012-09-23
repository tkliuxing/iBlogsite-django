#-*- coding: utf-8 -*-
from django import forms
from django_markdown.widgets import MarkdownWidget
from iblog.blog.models import Discuss


class DiscussForm(forms.ModelForm):
    class Meta:
        model = Discuss
        fields = ('name', 'email', 'content')
        widgets = {
            'content': MarkdownWidget(),
        }


class UserDiscussForm(forms.ModelForm):
    class Meta:
        model = Discuss
        fields = ('content',)
        widgets = {
            'content': MarkdownWidget(),
        }
