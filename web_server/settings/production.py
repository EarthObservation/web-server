import os

from .base import *


DEBUG = True  # Change to False in production
SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

ALLOWED_HOSTS = ['193.170.203.91']

# Check if PostgreSQL settings are set via environment variables
pgname = os.environ.get('POSTGRESQL_NAME', 'dridanube')
pguser = os.environ.get('POSTGRESQL_USER', 'dridanube')
pgpass = os.environ.get('POSTGRESQL_PASS', 'dridanube')
pghost = os.environ.get('POSTGRESQL_HOST', 'localhost')
pgport = int(os.environ.get('POSTGRESQL_PORT', 5432))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': pgname,
        'USER': pguser,
        'PASSWORD': pgpass,
        'HOST': pghost,
        'PORT': pgport,
        'CONN_MAX_AGE': 0,
    },
}
