from .base import *  # NOQA


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'viewsite',
        'USER': 'viewsite',
        'PASSWORD': 'viewsite',
        'HOST': '',
        'PORT': '',
    },
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
