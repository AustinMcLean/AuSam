from .settings_base import *

DEBUG = False

# 'default': dj_database_url.config(default='postgres://localhost')

DATABASES = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
}
