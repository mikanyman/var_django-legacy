import os, sys
sys.path.append('/var/django')
os.environ['DJANGO_SETTINGS_MODULE'] = 'coref.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
