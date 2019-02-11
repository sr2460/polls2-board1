#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from django.db import models
from django.utils import timezone



class Question(models.Model):
    class Meta:
        verbose_name_plural = '質問'

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    date_limit = models.DateTimeField('公開期限', default = timezone.now() + timedelta(days=7) )

    def is_date_limit(self):
        # まだ公開期限を過ぎていないならTrue
        now = timezone.now()
        return now <= self.date_limit


    def was_published_recently(self):
            now = timezone.now()
            return now - timedelta(days=1) <= self.pub_date <= now
            was_published_recently.admin_order_field = 'pub_date'
            was_published_recently.boolean = True
            was_published_recently.short_description = 'Published recently?'




class Choice(models.Model):
    class Meta:
        verbose_name_plural = '選択肢'

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Choice_Comment(models.Model):
    class Meta:
        verbose_name_plural = '選択肢のコメント'
        
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    choice_comment_text = models.TextField('コメント(未入力可)',blank=True, null=True)

    def __str__(self):
        return self.choice_comment_text
