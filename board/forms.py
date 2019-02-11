    #!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.views import generic
from .models import Post

class PostForm(forms.ModelForm):
    file = forms.FileField(required=False)
    #fileアップロード部分のラベルを消去
    file = forms.FileField(
        label='',
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'



    class Meta:
        model = Post
        fields = ('name', 'text', 'file')
