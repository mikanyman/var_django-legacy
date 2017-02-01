from django.conf.urls.defaults import *

urlpatterns = patterns('musa.frontpg.views',
    (r'yhteystiedot/$', 'yhteystiedot'),
    (r'audio/$', 'audio'),
    (r'bio/$', 'bio'),
    (r'styrman/$', 'styrman'),
    (r'/$', 'index'), # aina viimeiseksi

)