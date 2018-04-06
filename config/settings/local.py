from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iomb#911lo2we&991z=u(v)0)%d=mn6_3bh2s+$b7zo7pxcgzq'

DEBUG = env.bool('DJANGO_DEBUG', default=True)

ALLOWED_HOSTS = ['localhost']

