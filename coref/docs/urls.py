# coref/vdocs/urls.py

from django.conf.urls.defaults import *

urlpatterns = patterns('coref.docs.views',
    url(r'/$', 'index'),
    )
