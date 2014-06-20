"""
Django settings for quandi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n@k(v%=fn2wdxp-#5l*nak4m+%yd@pmgg4vx$dmy2ih6o0y5zf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

ADMINS = (('webmaster', 'webmaster@quandiwriting.com'))


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	 'testsite',
    'django.contrib.admin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'quandi.urls'

WSGI_APPLICATION = 'quandi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = '/home1/quandiwr/public_html/django/static/'
STATIC_URL = '/django/static/'


# authentication settings
LOGIN_REDIRECT_URL = '/profile/'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
PASSWORD_RESET_TIMEOUT_DAYS = 1

# upload settings
MEDIA_ROOT = '/home1/quandiwr/uploads/'
MEDIA_URL = '/media/'
FILE_UPLOAD_MAX_MEMORY_SIZE = 52428800

# email settings
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'mail.quandiwriting.com'
EMAIL_HOST_USER = 'webmaster@quandiwriting.com'
EMAIL_HOST_PASSWORD = '200180243quandiemail'
EMAIL_SUBJECT_PREFIX = '[Quandi] '
EMAIL_PORT = 465