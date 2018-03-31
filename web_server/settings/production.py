import os

from .base import *


DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
