from config.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_k(+z2g5upu@n03y-2vi$2dg23^1w0o^vevjrgpg56(b#+m-+7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition





SITE_ID = 3


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



STATIC_ROOT = BASE_DIR.joinpath('/static')

MEDIA_ROOT = BASE_DIR.joinpath('media')

STATICFILES_DIRS = [
    BASE_DIR/'static',
    BASE_DIR/'media',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

