from blog.settings.base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog',
        'USER': 'yunus',
        'PASSWORD': '1',
        'HOST': 'localhost',
        'PORT': '',
    }
}

ALLOWED_HOSTS = ['192.168.43.16']

# projeyi canlıda çalıştırken gerekiyor
# komut satırına python manage.py collectstatic yaz
STATIC_ROOT = os.path.join(BASE_DIR, 'static')