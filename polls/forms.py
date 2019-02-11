#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.db import models
from .models import Choice, Choice_Comment, Question
from django.shortcuts import get_object_or_404



class ChoiceCommentForm(forms.ModelForm):
    choice = forms.ModelChoiceField(
        queryset=Choice.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None,
        label=''
    )

    class Meta:
        model = Choice_Comment
        fields = ('choice', 'choice_comment_text')

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('target_question', None)
        super().__init__(*args, **kwargs)

        # choice の選択肢を question に関係したものに絞り込む
        if question:
            self.fields['choice'].queryset = Choice.objects.filter(question=question)


        for field in self.fields.values():
            field.widget.attrs['class'] = 'input-group-sm'

        class Meta:
            model = Choice_Comment
            fields = "__all__"
