from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
#from django_markdown import flatpages
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns(
    '',
    url(r'^$', 'iblog.homepage.views.homepage', name='home'),
    url(r'^login/$', 'iblog.homepage.views.login', name='login'),
    url(r'^logout/$', 'iblog.homepage.views.logout', name='logout'),
    url(r'^blog/(?P<blog>\d+)/$', 'iblog.blog.views.blog', name='blog'),
    url(r'^write/$', 'iblog.blog.views.write', name='blog_write'),
    url(r'^edit/(?P<blog_id>\d+)/$', 'iblog.blog.views.edit', name='blog_edit'),
    url(r'^discuss/(?P<discuss>\d+)/del/$', 'iblog.blog.views.discuss_del', name='disc_del'),
    url(r'^toupiao/', include('iblog.toupiao.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^tags/', include('universaltag.urls')),
)

from django.conf import settings

if settings.DEBUG:
    from django.views.generic import TemplateView
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += patterns(
        '',
        (r'^500\.html$', TemplateView.as_view(template_name="500.html")),
        (r'^404\.html$', TemplateView.as_view(template_name="404.html")),
    )
