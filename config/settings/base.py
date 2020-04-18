import os
from .apps import *
from .database import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get("DEBUG", True)

# Be carefull
ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


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


LANGUAGE_CODE = os.environ.get("LANGUAGE_CODE")

TIME_ZONE = os.environ.get("TIME_ZONE", "UTC")

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = os.environ.get("STATIC_URL")
STATIC_ROOT = os.environ.get("STATIC_ROOT")


# Django storages
DEFAULT_FILE_STORAGE = os.environ.get("DEFAULT_FILE_STORAGE")

# AWS credentials
# AWS_DEFAULT_ACL = None
AWS_STORAGE_BUCKET_URL = os.environ.get("AWS_STORAGE_BUCKET_URL")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME")
AWS_DEFAULT_ACL = os.environ.get("AWS_DEFAULT_ACL")

# Redis
BROKER = os.environ.get("BROKER")
BROKER_URL = os.environ.get("BROKER_URL")
