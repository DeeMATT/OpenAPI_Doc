"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from corsheaders.defaults import default_headers
import os
from dotenv import load_dotenv

from celery.schedules import crontab

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# ENV_PATH = BASE_DIR / 'envManager/.env'
ENV_PATH = BASE_DIR / 'envManager/envVariables.py'

load_dotenv(ENV_PATH)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

CRYPT_KEY = os.getenv('CRYPT_KEY')

# ROOT_SECRET = os.getenv('ROOT_SECRET')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

APPEND_SLASH = False

splittedHosts = os.getenv('ALLOWED_HOSTS').split(',')

ALLOWED_HOSTS = splittedHosts

# reset token time before expiry
DURATION = os.getenv('DURATION')

# Application definition
print('Starting app...')

SHARED_APPS = [
    'envManager',
    'channels',
    'swagger_render',
]

TENANT_APPS = [
    # The following Django contrib apps must be in TENANT_APPS
    'django.contrib.contenttypes',
    'corsheaders',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',

    # your tenant-specific apps

]

INSTALLED_APPS = list(SHARED_APPS) + \
    [app for app in TENANT_APPS if app not in SHARED_APPS]


# TENANT_MODEL = "tenants.Tenant"  # app.Model

# TENANT_DOMAIN_MODEL = "tenants.Domain"  # app.Model

MIDDLEWARE = [
    # 'django_tenants.middleware.main.TenantMainMiddleware',
    # 'django-tenants.middleware.SuspiciousTenantMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django_tenants.postgresql_backend',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

# DATABASE_ROUTERS = (
#     'django_tenants.routers.TenantSyncRouter',
# )

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

ASGI_APPLICATION = 'config.routing.application'

APPEND_SLASH = True

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False


CORS_ALLOW_HEADERS = list(default_headers) + [
    'accessToken',
    'secret'
]

# Celery config
CELERY_BROKER_URL = os.getenv('RABBIT_MQ_URL')

# Redis
REDIS_SERVER_NAME = os.getenv('REDIS_SERVER_NAME')
REDIS_PORT = os.getenv('REDIS_PORT')

# Email setup
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('SMTP_HOST')
EMAIL_HOST_USER = os.getenv('SMTP_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('SMTP_HOST_PASSWORD')
EMAIL_PORT = os.getenv('SMTP_PORT')
EMAIL_USE_TLS = os.getenv('SMTP_USE_TLS')

SWAGGER_YAML_FILENAME = '/swagger_render/docs/lola-api-doc.yml'

# wasabi s3 bucket configuration
BUCKET_ACCESS_KEY_ID = os.getenv('BUCKET_ACCESS_KEY_ID')
BUCKET_SECRET_KEY = os.getenv('BUCKET_SECRET_KEY')
BUCKET_REGION_NAME = os.getenv('BUCKET_REGION_NAME')
BUCKET_NAME = os.getenv('BUCKET_NAME')
BUCKET_ENDPOINT_URL = os.getenv('BUCKET_ENDPOINT_URL')

PASSWORD_RESET_ENDPOINT = os.getenv('PASSWORD_RESET_ENDPOINT')