# urlconf for synapse

from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to
from django.conf import settings

import os
cur_dir = os.getcwd()

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', redirect_to, {'url': '/en/company'}),
    (r'^en/$', redirect_to, {'url': '/en/company'}),
    #(r'^.{1}$', redirect_to, {'url': 'fi/'}),
    (r'^(?P<lang>\w{2})/', include('synapse.pages.urls')),
    #(r'^.{3,}$', redirect_to, {'url': 'fi/'}),
    (r'^segments/', include('synapse.segments.urls')),

    (r'^photologue/', include('photologue.urls')),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),    
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)


### Support for the tinymce-gallery-connection plugin
### http://code.google.com/p/tinymce-gallery-connection/

#from django.conf.urls.defaults import *
from views import *

urlpatterns += patterns('',
    (r'^galleries', galleries),
    (r'^images/(\-?\d+)', images),
    (r'^image/(\d+)', image),
    (r'^image_src/(\d+)/(\w+)', image_src),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )

if cur_dir.startswith('C:\\'):
    if settings.DEBUG:
        urlpatterns += patterns('',
            url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': 'C:/eclipse/workspace/a46.myrootshell.com/synapse/site_media'}),

            url(r'^js/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': 'C:/www/js'}),
                
            url(r'^admin_media/(.*)', 'django.views.static.serve',
                {'document_root' : 'C:/Python25/Lib/site-packages/django/contrib/admin/media'}),
        )
