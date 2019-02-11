#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .settings import *  # settings.pyの内容を全て引き継ぎ、ここから下に上書きしたいものを定義

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

DEBUG = False

ALLOWED_HOSTS = ['*']

STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_ROOT = '/usr/share/nginx/html/media'
