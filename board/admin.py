    #!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    search_fields = ['text']




admin.site.register(Post, PostAdmin)
