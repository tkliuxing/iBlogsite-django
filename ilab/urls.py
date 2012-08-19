from django.conf.urls import patterns, include, url
#from django_markdown import flatpages
from django.contrib import admin
admin.autodiscover()
#flatpages.register()
urlpatterns = patterns(
    '',
    url(r'^$', 'ilab.homepage.views.homepage', name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^tags/', include('universaltag.urls')),
)

from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns(
        'django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve', {'document_root': '/home/b/Code/website/iLab/ilab/static'}),
    )
