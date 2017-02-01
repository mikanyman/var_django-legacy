# dbxml/urls.py

from django.conf.urls.defaults import *

urlpatterns = patterns('coref.dbxml.views',
    url(r'/(?P<file>\w*)/(?P<param>\w*)/$', 'index'),
    url(r'/$', 'index'), # LAST
    )