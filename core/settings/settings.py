import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()


#  ------ One more parent directory to reach the project root ------>>
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ------- COMMON CODE FOR HANDLE MEDA, STATIC and TEMPLATES ---------
TEMPLATE_DIR = os.path.join(BASE_DIR , 'templates')
MEDIA_DIR = os.path.join(BASE_DIR , 'media')
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR

# -------------=====> EXTRA <=====------------------
AUTH_USER_MODEL = 'app_users.User'
LOGIN_URL = "/auth/login/"
# --------------------========----------------------



SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret-key')
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')

INSTALLED_APPS = [
    # ------- Created and 3rd party apps ---------
    'daphne',
    'channels',
    'django_htmx',
    'social_django',

    'apps.app_users',
    'apps.app_chat',
    'apps.app_home',
    'apps.app_account',
    
    # --------- In Built Apps ---------
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_htmx.middleware.HtmxMiddleware",
]
ROOT_URLCONF = 'core.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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


#  -========- Django Websocket Setup -==========-

# ASGI_APPLICATION = "core.asgi.application" # your project name

# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer", # Or other backend
#         "CONFIG": {
#             "hosts": [("127.0.0.1", 6379)], #  Redis server
#         },
#     },
# }

# WSGI_APPLICATION = 'core.wsgi.application'
ASGI_APPLICATION = 'core.asgi.application'


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}
# -------------------------------------------------



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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#  --------================ LOAD =============------------
from ..credentials.cloud_storage  import *
from ..credentials.oauth import *
from ..credentials.payment_or_error import *

from .mail_settings import *

LIVE_SITE_URL_RN=os.getenv('LIVE_SITE_URL_RN', 'http://localhost:8000/')