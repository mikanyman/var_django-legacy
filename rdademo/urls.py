from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'rdademo.views.home', name='home'),
    url(r'^rda/', include('rdademo.rda.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
