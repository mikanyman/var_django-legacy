from django.conf.urls.defaults import *

urlpatterns = patterns('maisemat.frontpg.views',
    url(r'^$', 'etusivu', name='etusivu'),
    url(r'^kuvat/$', 'yhteystiedot', name='kuvat'),
    url(r'^dokumentit/$', 'dokumentit', name='dokumentit'),
    url(r'^kalenteri/$', 'kalenteri', name='kalenteri'),
    url(r'^yhteystiedot/$', 'yhteystiedot', name='yhteystiedot'),
    url(r'^kieli/$', 'kieli', name='kieli'),    
)