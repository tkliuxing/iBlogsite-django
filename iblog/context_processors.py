# -*- coding: utf-8 -*-
from django.conf import settings
from universaltag.models import Tag


def site_env(request):
    site_name = getattr(settings, 'SITE_NAME', '')
    return {'SITE_ENV': {'SITE_NAME': site_name}}


def request(request):
    return {'request': request}


def google_analytics(request):
	return {'GA_CODE': getattr(settings, 'GA_CODE', '')}


def tag_manager(request):
	tag_styles = [
		'',
		'label-success',
		'label-warning',
		'label-important',
		'label-info',
		'label-inverse',
	]
	return {'tagmanager': Tag.objects, 'tag_styles': tag_styles}
