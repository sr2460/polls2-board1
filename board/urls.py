
    #!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from . import views

app_name = 'board'
urlpatterns = [
    path('', views.ListView.as_view(), name='board'),
    path('good/<int:pk>', views.good, name='good'),
]
