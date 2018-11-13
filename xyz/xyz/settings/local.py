from .base import *

SECRET_KEY = env('SECRET_KEY')

DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': env.db()
}