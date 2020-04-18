import os
import sys

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_NAME_READ = os.environ.get("DB_NAME_READ")
DB_NAME_WRITE = os.environ.get("DB_NAME_WRITE")
DB_USER_READ = os.environ.get("DB_USER_READ")
DB_USER_WRITE = os.environ.get("DB_USER_WRITE")
DB_PASSWORD_READ = os.environ.get("DB_PASSWORD_READ")
DB_PASSWORD_WRITE = os.environ.get("DB_PASSWORD_WRITE")
DB_HOST_READ = os.environ.get("DB_HOST_READ")
DB_HOST_WRITE = os.environ.get("DB_HOST_WRITE")

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


DATABASES = {
    'default': {
        'NAME': DB_NAME_READ,
        'ENGINE': 'django.db.backends.mysql',
        'USER': DB_USER_READ,
        'PASSWORD': DB_PASSWORD_READ,
        'HOST': DB_HOST_READ,
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    },
    'read': {
        'NAME': DB_NAME_READ,
        'ENGINE': 'django.db.backends.mysql',
        'USER': DB_USER_READ,
        'PASSWORD': DB_PASSWORD_READ,
        'HOST': DB_HOST_READ,
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    },
    'write': {
        'NAME': DB_NAME_WRITE,
        'ENGINE': 'django.db.backends.mysql',
        'USER': DB_USER_WRITE,
        'PASSWORD': DB_PASSWORD_WRITE,
        'HOST': DB_HOST_WRITE,
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    },
}

if 'test' in sys.argv:
    DATABASES['write'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'write'
    }
    DATABASES['read'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'read'
    }
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'default'
    }

# https://docs.djangoproject.com/en/3.0/topics/db/multi-db/
DATABASE_ROUTERS = [
    'config.database_routers.read_router.ReadRouter',
    'config.database_routers.write_router.WriteRouter'
]
