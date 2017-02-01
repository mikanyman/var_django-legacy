from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'coref.docs.views.index'),
    (r'^kmm/geomaster',  include('coref.geomaster.urls')),
    (r'^kmm',  include('coref.geomaster.urls')),
    (r'^pages/', include('pages.urls')),
    (r'^photologue/', include('photologue.urls')),
    (r'^pressroom/', include('pressroom.urls')),
    
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),

)
