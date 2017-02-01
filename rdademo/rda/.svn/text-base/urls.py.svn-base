## rdademo/rda/urls.py

from django.conf.urls.defaults import *

#urlpatterns = patterns('specs.frontpg.views',
urlpatterns = patterns('rdademo.rda.views',
    url(r'^(?P<url_cls>\w+)/$', 'index'),
    url(r'^(?P<url_cls>\w+)/attributes/add/$', 'add'),
    url(r'^(?P<url_cls>\w+)/relations/(?P<query>\d+)/$', 'relations'),
	url(r'^(?P<url_cls>\w+)/instances/$', 'instances'),
    url(r'^(?P<url_cls>\w+)/search/(?P<query>\d+)/$', 'relations'),
	
    url(r'^search/(?P<query>\w+)$', 'kysely'),
	
    #url(r'^(?P<url_pg>\w*)/(?P<url_id>\d+)/$', 'index_id'),                                       
    #url(r'^(?P<url_pg>vaikuta)/poll/(?P<poll_id>\d+)/kiitos/$', 'poll'),
    #url(r'^(?P<url_pg>vaikuta)/$', 'cur_poll'),
    #url(r'^(?P<url_pg>vaikuta)/\d+/$', 'cur_poll'),
    #url(r'^(?P<url_pg>vaikuta)/polls/(?P<url_id>\d+)/$', 'poll'),
)
