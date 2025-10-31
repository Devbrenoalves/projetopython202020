from .settings import *

DEBUG = os.getenv("DEBUG", "True")

if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Não importe S3
# from ..credentials.cloud_storage import *

# Configure armazenamento local
MEDIA_DIR = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
MEDIA_ROOT = MEDIA_DIR

DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
