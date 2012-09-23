from django.conf.urls import patterns, include, url
#from django_markdown import flatpages
from django.contrib import admin
admin.autodiscover()
#flatpages.register()
urlpatterns = patterns(
    '',
    url(r'^$', 'iblog.homepage.views.homepage', name='home'),
    url(r'^blog/(?P<blog>\d+)/$', 'iblog.blog.views.blog', name='blog'),
    url(r'^discuss/(?P<discuss>\d+)/del/$', 'iblog.blog.views.discuss_del', name='disc_del'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^tags/', include('universaltag.urls')),
)

from django.conf import settings

if settings.DEBUG:
    from django.views.generic import TemplateView
    urlpatterns += patterns(
        'django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve', {'document_root': '/home/b/Code/website/iblog/iblog/static'}),
    )
    urlpatterns += patterns(
        '',
        (r'^500\.html$', TemplateView.as_view(template_name="500.html")),
        (r'^404\.html$', TemplateView.as_view(template_name="404.html")),
    )
