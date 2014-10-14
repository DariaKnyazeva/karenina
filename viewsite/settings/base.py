import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


# Applications

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'viewsite.modules',
    'viewsite.website',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'viewsite.urls'

WSGI_APPLICATION = 'viewsite.wsgi.application'

ALLOWED_HOSTS = []

# Templates

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
    }
}


# Internationalization

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'deploy/static')


# Media

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'deploy/media')
