from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', redirect_to, {'url': '/en/about/'}), # flatpage
    (r'^\w{2}/$', redirect_to, {'url': '/en/about/'}), # flatpage
    (r'^i18n/', include('django.conf.urls.i18n')),    
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)