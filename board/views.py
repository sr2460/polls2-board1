    #!/usr/bin/env python
# -*- coding: utf-8 -*-

from .models import Post
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.views import generic
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import ModelFormMixin
from django.http import JsonResponse

import sys
sys.path.append('../')
from polls.models import Question



class ListView(generic.ListView, ModelFormMixin):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('board:board')
    template_name = 'board/board.html'
    paginate_by = 15


    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def get_queryset(self):
        return Post.objects.order_by('-date')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = Question.objects.all()
        return context


def good(request, pk):
    """いいねボタンをクリック."""
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        # データの新規追加
        post.good += 1
        post.save()

    return redirect('board:board')
