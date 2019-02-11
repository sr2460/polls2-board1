    #!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone

class Post(models.Model):
    class Meta:
        verbose_name = '投稿'
        verbose_name_plural = '投稿リスト'

    name = models.CharField('名前', max_length=20, default='ベルマーレ大好き')
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)
    file = models.FileField('ファイル', null=True,)
    good = models.IntegerField(default=0)

    def __str__(self):
        return self.text
