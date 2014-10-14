from .base import *  # NOQA


# Applications

SECRET_KEY = '5maw1+0b03(jqy#dvsoudpx_59-6dpx2qy5io)cy_vrev8z$wx'

DEBUG = True
TEMPLATE_DEBUG = True


# Databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'viewsite',
        'USER': 'viewsite',
        'PASSWORD': 'viewsite',
        'HOST': '',
        'PORT': '',
    }
}

# Email

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
