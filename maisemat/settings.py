# Django settings for maisemat project.
import os
from django.utils.translation import gettext_lazy as _

cur_dir = os.getcwd()

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'postgresql_psycopg2'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'maisemat'                            # maisemat
DATABASE_USER = 'maisemat'                            # maisemat
DATABASE_PASSWORD = 'maisemat'                        # maisemat
DATABASE_HOST = '127.0.0.1'                       # 127.0.0.1
DATABASE_PORT = '5432'                            # 5432

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Helsinki'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fi' # 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
if cur_dir == '/':
    MEDIA_ROOT = '/var/django/maisemat/media/'
elif cur_dir.startswith('C:\\'):
    MEDIA_ROOT = 'C:/eclipse/workspace/a46.myrootshell.com/maisemat/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
if cur_dir == '/':
     MEDIA_URL = 'http://matkamaisemaan.coreference.org/site_media/'
elif cur_dir.startswith('C:\\'):
     MEDIA_URL = 'http://127.0.0.1:8000/site_media/'
# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'h64oad--e=i2*zew34y59r!+e5_k@s97tm=tfo_wg$^@vq5f%t'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#   'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'maisemat.middleware.SetLangFi',
)

LANGUAGE_COOKIE_NAME = 'django_language'

LANGUAGES = (
    ('fi', _('Finnish')),
    ('en', _('English')),
)
    
ROOT_URLCONF = 'maisemat.urls'

# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
if cur_dir == '/':
    TEMPLATE_DIRS = (
        '/var/django/maisemat/templates'
    )
elif cur_dir.startswith('C:\\'):
    TEMPLATE_DIRS = (
        'C:/eclipse/workspace/a46.myrootshell.com/maisemat/templates'
    )

# django-registration
ACCOUNT_ACTIVATION_DAYS = 7
EMAIL_HOST='localhost'
DEFAULT_FROM_EMAIL = 'info@synapse-computing.com'
LOGIN_REDIRECT_URL = '/'

# django-profiles
AUTH_PROFILE_MODULE = 'profile.MaisematProfile'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'maisemat.profile',
    'profiles',
    'registration',
)
