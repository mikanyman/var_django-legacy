# Import django modules
from django.conf.urls.defaults import *


urlpatterns = patterns('geodemo.waypoints.views',
                       url(r'^$', 'index', name='waypoints-index'),
					   url(r'^saveFromMatkain$', 'saveFromMatkain', name='matkain-save'),
                       )
