#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Choice, Question, Choice_Comment

#modelsからインポート
#管理サイトのテキストの初期選択数
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

#管理サイトのサーチ機能
class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]

class ChoiceAdmin(admin.ModelAdmin):
    list_filter = ['question']



class Choice_CommentAdmin(admin.ModelAdmin):
    list_filter = ['question']



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Choice_Comment, Choice_CommentAdmin)
