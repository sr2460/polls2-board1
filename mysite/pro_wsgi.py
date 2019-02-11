#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from django.core.wsgi import get_wsgi_application

# pro_settings.pyを使うように指定
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.pro_settings")

application = get_wsgi_application()
