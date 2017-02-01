from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'coref.docs.views.index'),
    
    (r'^kmm/geomaster',  include('coref.geomaster.urls')),
    (r'^kmm',  include('coref.geomaster.urls')),
    #(r'^dbxml',  include('coref.dbxml.urls')),
    
    (r'^fm/', include('coref.fileman.urls')),
    
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
