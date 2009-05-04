# Django settings for touchdown project.

from localsettings import *
# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'touchdown.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.gis',
    'django_openid_auth',
    'django_evolution',
    'touchdown.referee',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_openid_auth.auth.OpenIDBackend',
)

GAME_POINT_COUNT=40

OPENID_CREATE_USERS = True

OPENID_UPDATE_DETAILS_FROM_SREG = True

LOGIN_URL = '/openid/login'

LOGIN_REDIRECT_URL = '/'

REQUIRE_TOUCHDOWN_APPROVAL = False