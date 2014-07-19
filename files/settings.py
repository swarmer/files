"""
Django settings for files project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import socket

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', '1') == '1'

# SECURITY WARNING: keep the secret key used in production secret!
if DEBUG:
    SECRET_KEY = 'n4k+i6&sp9%)5thl!#5pfd#htmp+8**=ken+*w*kj4sa_^0mnn'
else:
    with open(os.path.join(BASE_DIR, '..', 'key')) as key_file:
        SECRET_KEY = key_file.read()

TEMPLATE_DEBUG = DEBUG

if DEBUG:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = ['files.%s' % socket.gethostname()]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
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

ROOT_URLCONF = 'files.urls'

WSGI_APPLICATION = 'files.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

if DEBUG:
    db = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
else:
    db = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': '',
        'NAME': 'files',
        'USER': 'files',
    }

DATABASES = {
    'default': db
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
if not DEBUG:
    STATIC_ROOT = os.environ['STATIC_ROOT']


# Media files

MEDIA_URL = '/f/'
if DEBUG:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
else:
    MEDIA_ROOT = os.environ['MEDIA_ROOT']
