#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import  ChoiceCommentForm
from .models import Choice, Question, Choice_Comment
from django.views.generic.edit import ModelFormMixin



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    paginate_by = 20

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')


class DetailView(ModelFormMixin, generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    form_class = ChoiceCommentForm

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

    def dispatch(self, request, *args, **kwargs):
        self.target_question = get_object_or_404(Question, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['target_question'] = self.target_question
        return kwargs




class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'




def vote(request, question_id):
    form = ChoiceCommentForm(request.POST or None)
    question = get_object_or_404(Question, pk=question_id)


    if request.method == 'POST':
        if form.is_valid():
            selected_choice= question.choice_set.get(pk=request.POST['choice'])
            selected_choice.votes += 1
            selected_choice.save()
            choice_comment = form.save(commit=False)  # コメントはDBに保存されていません
            choice_comment.question = question
            choice_comment.save()  # ここでDBに保存
            return redirect('polls:results', pk=question_id)

        context = {
            'question': question,
            'form': form,
            'error_message': "投票内容を選んでください",
        }
        return render(request, 'polls/detail.html', context)


def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]



def commentlist(request, pk):
    question = get_object_or_404(Question, pk=pk) #コンテキストでpk渡さないとquestion.pkでリンクが飛ばない。
    comment_filter = get_object_or_404(Question, pk=pk)
    context = {
    'comment_ichiran':Choice_Comment.objects.filter(question=comment_filter).exclude(choice_comment_text__exact=""),
    'question':question
    }
    return render(request, 'polls/comment_list.html', context)
