from os import environ
from .base import *  # NOQA


# Host configuration

ALLOWED_HOSTS = []
SECRET_KEY = environ.get('SECRET_KEY')


# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'viewsite',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}


# Email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'your_email@example.com')
EMAIL_PORT = environ.get('EMAIL_PORT', 587)
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER
