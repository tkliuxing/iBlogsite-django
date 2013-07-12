from django.conf.urls import patterns, url
urlpatterns = patterns(
    'iblog.toupiao.views',
    url(r'^$', 'toupiao', {'template': 'toupiao.html'}, name='toupiao'),
    url(r'^(?P<toupiao_id>\d+)/xiangmu/$', 'create_xiangmu', name='xinxiangmu'),
    url(r'^(?P<toupiaoxiang_id>\d+)/plusone/$', 'plus_one', name='plusone')
)