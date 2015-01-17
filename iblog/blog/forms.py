#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django_markdown.widgets import MarkdownWidget
from django.utils.translation import ugettext as _
from iblog.blog.models import Discuss, Blog


class BlogForm(forms.ModelForm):
    tags = forms.CharField(
        label=_('Tags'),
        max_length=100,
        required=False,
        help_text=_('逗号分割的词'))

    class Meta:
        model = Blog
        fields = ('title', 'content',)
        widgets = {
            'content': MarkdownWidget(),
        }

class BlogEditForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content',)
        widgets = {
            'content': MarkdownWidget(),
        }

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
