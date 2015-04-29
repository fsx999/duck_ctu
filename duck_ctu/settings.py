"""
Django settings for duck_inscription project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

# coding=utf-8
import os

from django.conf.global_settings import gettext_noop

DEBUG = True

TEMPLATE_DEBUG = True
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ALLOWED_HOSTS = []
LANGUAGES = (('fr', gettext_noop('French')),)
DATE_FORMAT = "d/m/Y"
DATE_INPUT_FORMATS = ("%d/%m/%Y",)
SHORT_DATETIME_FORMAT = "d/m/Y"
STATIC_ROOT = os.path.join(BASE_DIR, '../static').replace('\\', '/')
MEDIA_ROOT = os.path.join(BASE_DIR, '../static_tel').replace('\\', '/')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates').replace('\\', '/'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                "django.core.context_processors.request",
            ],
            'loaders': [
                 'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'duck_utils.loaders.Loader',
            ]
        },
    },
]
# Application definition

INSTALLED_APPS = (
    'xadmin',
    'crispy_forms',
    'django_xworkflows.xworkflow_log',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'duck_inscription',
    'django_extensions',
    'django_apogee',
    'registration',
    'captcha',
    'compressor',
    'floppyforms',
    'django_xworkflows',
    'autocomplete_light',
    'wkhtmltopdf',
    'xhtml2pdf',
    'mailrobot',
    'django.contrib.sites',
    'django.contrib.humanize',
    'mptt',
    'openpyxl',
    "duck_utils"
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = False  # Important, toujours False



STATIC_URL = '/static/'

COMPRESS_OFFLINE = False

ACCOUNT_ACTIVATION_DAYS = 1

MEDIA_URL = '/static_tel/'


SITE_ID = 1
TARIF_MEDICAL = 5.10
TARIF_SECU = 213
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'deh*%fl_7p&+5^(ry7116z&^-)nzyi#_iaww__6^i7m#-%3bsl'

# SECURITY WARNING: don't run with debug turned on in production!

ROOT_URLCONF = 'duck_ctu.urls'

WSGI_APPLICATION = 'duck_ctu.wsgi.application'

LOGIN_URL = 'auth_login'

WKHTMLTOPDF_CMD = BASE_DIR+'/wkhtmltopdf'
SILENCED_SYSTEM_CHECKS = [
    'fields.W340',
    'fields.W342'
]
try:
    import local_settings
    from local_settings import *

except ImportError:
    local_settings = object
try:
    if DEBUG:
        DEV_APPS = getattr(local_settings, 'DEV_APPS', ())
        INSTALLED_APPS += DEV_APPS
        MIDDLEWARE_CLASSES = ('debug_toolbar.middleware.DebugToolbarMiddleware',) +\
                              MIDDLEWARE_CLASSES + ('devserver.middleware.DevServerMiddleware',)
    INSTALLED_APPS = getattr(local_settings, 'FIRST_APPS', ()) + INSTALLED_APPS + getattr(local_settings,
                                                                                          'LAST_APPS', ())

except NameError:
    print "erreur"

if DEBUG:
    COMPRESS_ENABLED = False
else:
    COMPRESS_ENABLED = False

AUTH_USER_MODEL = 'duck_inscription.InscriptionUser'
