# Django settings for europeana project.
from django.utils.translation import gettext_lazy as _

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Mika Nyman', 'mika.nyman@synapse-computing.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'postgresql_psycopg2'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'europeana'             # Or path to database file if using sqlite3.
DATABASE_USER = 'europeana'             # Not used with sqlite3.
DATABASE_PASSWORD = 'europeana'         # Not used with sqlite3.
DATABASE_HOST = '127.0.0.1'             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = '5432'             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Amsterdam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/var/django/europeana/site_media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://europeana.coreference.org:8080/europeana/site_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'lbj%0-7jma4^*f==$xv===(ug-_4-pss%gt1txsxsl$0fg0(=j'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

LANGUAGE_COOKIE_NAME = 'django_language'

LANGUAGES = (
    ('bg', '(bul)'),
    ('ca', '(ca)'),
    ('cs', '(cze/cs)'),
    ('da', '(dan)'),
    ('de', '(deu)'),
    ('el', '(ell/gre)'),
    ('en', '(eng)'),
    ('es', '(esp)'),
    ('et', '(est)'),
    ('fi', '(fin)'),
    ('fr', '(fre)'),
    ('ga', '(gle)'),
    ('hu', '(hun)'),
    ('is', '(ice)'),
    ('it', '(ita)'),
    ('lt', '(lit)'),
    ('lv', '(lav)'),
    ('mt', '(mlt)'),
    ('nl', '(dut)'),
    ('no', '(nor)'),
    ('pl', '(pol)'),
    ('pt', '(por)'),
    ('ro', '(rom)'),
    ('sk', '(slo)'),
    ('sl', '(slv)'),
    ('sv', '(sve/swe)'),
)

ROOT_URLCONF = 'europeana.urls'

TEMPLATE_DIRS = (
    '/var/django/europeana/templates'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.sites',
)
