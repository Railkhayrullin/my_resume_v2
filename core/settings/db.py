import os

#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
#         'NAME': os.environ.get('POSTGRES_DB', 'postgres'),
#         'USER': os.environ.get('POSTGRES_USER', 'postgres'),
#         'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
#         'PORT': os.environ.get('POSTGRES_PORT', '5432'),
#     }
# }
from core.settings.general import BASE_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
