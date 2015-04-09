
import os
DEBUG = True


TEMPLATE_DEBUG = True
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ALLOWED_HOSTS = []
LANGUAGES = (
    ('fr', 'France'),
)
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
    'duck_bo_ctu',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
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
    'openpyxl',
    'duck_utils',
    'reversion'
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


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'deh*%fl_7p&+5^(ry7116z&^-)nzyi#_iaww__6^i7m#-%3bsl'


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ROOT_URLCONF = 'duck_ctu.bo_urls'

WSGI_APPLICATION = 'duck_ctu.bo_wsgi.application'


LOGIN_URL = '/'
SITE_ID = 2
SITE_ID_IED = 1


WKHTMLTOPDF_CMD = BASE_DIR+'/wkhtmltopdf'
try:
    import bo_local_settings
    from bo_local_settings import *

except ImportError:
    bo_local_settings = object
    print "pas de local settings"

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




