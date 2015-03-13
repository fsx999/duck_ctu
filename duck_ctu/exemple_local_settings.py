# coding=utf-8
import re
EMAIL_HOST = ''
EMAIL_USE_TLS = True
EMAIL_PORT = 2525
EMAIL_HOST_USER = "" # a remplir
EMAIL_HOST_PASSWORD = ""
DEBUG = True
ALLOWED_HOSTS = ['']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.

    },
    'oracle': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': '',
        'USER': '',
        # 'USER': 'WEBIED',
        # 'PASSWORD': 'WEBIED',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },

}
APOGEE_CONNECTION = ""
COD_CGE = ""
COMPOSANTE = '' # a remplir
INTERNAL_IPS = ('127.0.0.1',)
DEV_APPS = ('devserver', 'debug_toolbar')
