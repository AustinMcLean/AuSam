from .settings_base import *

DEBUG = True


DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.postgresql',
        #'NAME': 'guestsDB',
        #'USER': os.environ.get('POSTGRES_USER'),
        #'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        #'HOST': 'localhost',
        #'PORT': '5432',
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
