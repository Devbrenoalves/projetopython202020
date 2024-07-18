import os
from pathlib import Path

# ------- COMMON CODE FOR HANDLE MEDA, STATIC and TEMPLATES ---------
DEBUG = True
BASE_DIR = Path(__file__).resolve().parent.parent
if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

TEMPLATE_DIR = os.path.join(BASE_DIR , 'templates')
MEDIA_DIR = os.path.join(BASE_DIR , 'media')

STATIC_URL = 'static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = MEDIA_DIR


# --=====> EXTRA <=====------

AUTH_USER_MODEL = 'app_users.User'
LOGIN_URL = "/auth/login/"
# ---------======== ----------

#  --------------------------==========-------------------------------

SECRET_KEY = 'django-insecure-&8$jipu$mg1ap2l!lv0fxu7^br^*341squ(uv(-z8=1#$_*_1-'
ALLOWED_HOSTS = ["localhost","127.0.0.1"]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_users',
    'app_chat',
    'app_home',
    'django_htmx',
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
WSGI_APPLICATION = 'core.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'ashiqmyi_chatxity',
#         'USER': 'ashiqmyi@localhost',
#         'PASSWORD': '7102000@@@@@@',  # Replace with your actual password
#         'HOST': 'localhost',  # Adjust if needed
#         'PORT': '3306',
#     }
# }


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
