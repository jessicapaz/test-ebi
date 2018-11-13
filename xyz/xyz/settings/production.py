from .base import *

SECRET_KEY = env('SECRET_KEY')

DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = ['.herokuapp.com']

DATABASES = {
    'default': env.db()
}