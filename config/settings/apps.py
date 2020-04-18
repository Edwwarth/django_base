DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    # 'rest_framework',
    # 'django_celery_results',
    # 'storages',
    # 'django_nose',
    # 'corsheaders',
    # 'oauth2_provider',
]

LOCAL_APPS = [
    # 'biometric.v1.core',
    # 'biometric.v1.parametrics',
    # 'biometric.v1.liveness',
    # 'biometric.v1.interview',
    # 'biometric.v1.account',
    # 'biometric.v1.transaction',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

DJANGO_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]
THIRD_PARTY_MIDDLEWARE = [
    # 'corsheaders.middleware.CorsMiddleware',
]

MIDDLEWARE = DJANGO_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE