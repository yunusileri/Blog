from blog.settings.base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '../../static')
]

# projeyi canlıda çalıştırken gerekiyor
# komut satırına python manage.py collectstatic yaz
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')

ALLOWED_HOSTS = []