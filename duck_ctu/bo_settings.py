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


# Application definition

INSTALLED_APPS = (
    'xadmin',
    'crispy_forms',
    'django_xworkflows.xworkflow_log',
    'duck_theme_ied',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # 'django.contrib.sites',
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
    'django_nyt',
    # 'django_notify',
    'mptt',
    'sekizai',
    'sorl.thumbnail',
    'wiki',
    'wiki.plugins.attachments',
    'wiki.plugins.notifications',
    'wiki.plugins.images',
    'wiki.plugins.macros',
    'linaro_django_pagination',
    'djangobb_forum',
    'haystack',
    'openpyxl',
    'foad',
    "django_mptt_admin",
    "duck_svi",
    'gestion_info',
    'macaddress',
    'markdown_deux',
    'helpdesk',
    'bootstrapform',
    "duck_paiement_etudiant",
    'duck_examen',
    'duck_utils',
    'reversion',
    'ckeditor',
    'duck_ied'
)
from django import VERSION
if VERSION < (1, 7):
    INSTALLED_APPS += ('south', )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'linaro_django_pagination.middleware.PaginationMiddleware',
    # 'djangobb_forum.middleware.LastLoginMiddleware',
    # 'djangobb_forum.middleware.UsersOnline',
    # 'djangobb_forum.middleware.TimezoneMiddleware',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'duck_utils.loaders.Loader',
    # 'django.template.loaders.eggs.Loader',


)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)


SOUTH_DATABASE_ADAPTERS = {
    'default': 'south.db.postgresql_psycopg2',
    'oracle': 'south.db.sqlite3',
    'oracle_test': 'south.db.sqlite3',
}

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = False  # Important, toujours False


STATIC_URL = '/static/'

COMPRESS_OFFLINE = False

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates').replace('\\', '/'),
)

ACCOUNT_ACTIVATION_DAYS = 1
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "sekizai.context_processors.sekizai",
    'djangobb_forum.context_processors.forum_settings',
)
MEDIA_URL = '/static_tel/'
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'djangobb_index'),
        'INCLUDE_SPELLING': True,
    },
}
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# DATABASE_ROUTERS = ['duck_svi.routers.SviRouter',]
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 1300,
        'basicEntities': False,
        'entities': False,
        'htmlbase': False,
        'entities_latin': False,
        'entities_greek': False,
        'removeFormatTags': '',
        'removeFormatAttributes': '',
        'autoParagraph': False,
        'fullPage': True,
        'protectedSource': ['/{% load .* %}'],
        'contentsLanguage': 'fr',
        "removePlugins": "stylesheetparser",
        'allowedContent': True,
        'clipboard_defaultContentType': 'text',
        'fillEmptyBlocks': False,
        'forcePasteAsPlainText': True,

    },
}



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'deh*%fl_7p&+5^(ry7116z&^-)nzyi#_iaww__6^i7m#-%3bsl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ROOT_URLCONF = 'test_duck_inscription.bo_urls'

WSGI_APPLICATION = 'test_duck_inscription.bo_wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LOGIN_URL = '/'

from django.conf import settings
TEMPLATE_CONTEXT_PROCESSORS = settings.TEMPLATE_CONTEXT_PROCESSORS + ("django.core.context_processors.request",)
WKHTMLTOPDF_CMD = BASE_DIR+'/wkhtmltopdf'
try:
    import bo_local_settings
    from bo_local_settings import *

except ImportError:
    bo_local_settings = object
    print "pas de local settings"
SITE_ID = 2
SITE_ID_IED = 1

try:
    if DEBUG:
        DEV_APPS = getattr(bo_local_settings, 'DEV_APPS', ())
        INSTALLED_APPS += DEV_APPS
        MIDDLEWARE_CLASSES = ('debug_toolbar.middleware.DebugToolbarMiddleware',) +\
                              MIDDLEWARE_CLASSES + ('devserver.middleware.DevServerMiddleware',)
    INSTALLED_APPS = getattr(bo_local_settings, 'FIRST_APPS', ()) + INSTALLED_APPS + getattr(bo_local_settings,
                                                                                          'LAST_APPS', ())

except NameError:
    print "erreur"
if DEBUG:
    COMPRESS_ENABLED = False
else:
    COMPRESS_ENABLED = False




USE_TZ = True
LANGUAGES = (
    ('fr', 'France'),
)
## setting djangobb_forum
DJANGOBB_HEADER = 'Accueil forum'
DJANGOBB_TAGLINE = 'Forum de l\'IED'
DJANGOBB_FORUM_BASE_TITLE = 'IED forum'

HELPDESK_VIEW_A_TICKET_PUBLIC = False
HELPDESK_SUBMIT_A_TICKET_PUBLIC = False
HELPDESK_CREATE_TICKET_HIDE_ASSIGNED_TO = True