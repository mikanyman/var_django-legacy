# kmm/geomaster/urls.py

from django.conf.urls.defaults import *

urlpatterns = patterns('coref.geomaster.views',
    url(r'lan/$', 'lan'),
    url(r'kommuner/$', 'kommuner'),
    url(r'landskap/$', 'landskap'),
    url(r'socknar/$', 'socknar'),
    url(r'/$', 'lan'), # LAST
    )
