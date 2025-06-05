from .settings import *

DEBUG = os.getenv("DEBUG", "True")

if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')



# ----- in pythonanwhere Using SQLite Database Setup ------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



# ------- MYSQL Database Setup ------------
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': '',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',
#     }
# }


# ----- PostgreSQL Database Setup ------------
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('DB_NAME', 'your_db_name'),
#         'USER': os.getenv('DB_USER', 'your_db_user'),
#         'PASSWORD': os.getenv('DB_PASSWORD', 'your_db_password'),
#         'HOST': os.getenv('DB_HOST', 'localhost'),
#         'PORT': os.getenv('DB_PORT', '5432'),
#     }
# }




# ============== STORAGE SETTINGS (NOT USING NOW )==============

# STORAGES = {
#     "default": {
#         "BACKEND": "storages.backends.s3.S3Storage",
#         "OPTIONS": {
#             "access_key": AWS_ACCESS_KEY_ID,
#             "secret_key": AWS_SECRET_ACCESS_KEY,
#             "bucket_name": AWS_STORAGE_BUCKET_NAME,
#             "endpoint_url": AWS_S3_ENDPOINT_URL,
#             "location": AWS_LOCATION,
#             "default_acl": AWS_DEFAULT_ACL,
#             "querystring_auth": False,
#         },
#     },
#     'staticfiles': {
#         "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
#     }
# }
