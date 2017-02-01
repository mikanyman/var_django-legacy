import os
cur_dir = os.getcwd()
from maisemat import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('maisemat.frontpg.urls')),
    url(r'^accounts/', include('registration.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if cur_dir.startswith('C:\\'):
    if settings.DEBUG:
        urlpatterns += patterns('',
            url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': 'C:/eclipse/workspace/a46.myrootshell.com/maisemat/media'}),
                
            url(r'^admin_media/(.*)', 'django.views.static.serve',
                {'document_root' : 'D:/Python26/Lib/site-packages/django/contrib/admin/media'}),
        )