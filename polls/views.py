from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from polls.models import Question, Choice

# Create your views here.
class QuestionListView(generic.ListView):
    template_name = 'polls/question/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.get_latest()


class QuestionDetailView(generic.DetailView):
    model = Question

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/question/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
