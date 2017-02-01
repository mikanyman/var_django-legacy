# Import django modules
from django.conf.urls.defaults import *
from django.contrib import admin
import settings

admin.autodiscover()
urlpatterns = patterns('',
    (r'^admin/',   include(admin.site.urls)),
    (r'^', include('geodemo.waypoints.urls')),
)
