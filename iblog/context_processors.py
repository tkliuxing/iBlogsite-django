# -*- coding: utf-8 -*-
from django.conf import settings


def site_env(request):
    site_name = getattr(settings, 'SITE_NAME', '')
    return {'SITE_ENV': {'SITE_NAME': site_name}}


def request(request):
    return {'request': request}
