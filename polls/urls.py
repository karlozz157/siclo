from django.urls import path

from polls.views import QuestionListView, QuestionDetailView, vote

app_name = 'polls'

urlpatterns = [
    path(
        route='', 
        view=QuestionListView.as_view(),
        name='index'
    ),
    path(
        route='<int:pk>/', 
        view=QuestionDetailView.as_view(template_name='polls/question/detail.html'),
        name='detail'
    ),
    path(
        route='<int:pk>/results/',
        view=QuestionDetailView.as_view(template_name='polls/question/results.html'),
        name='results'
    ),
    path(
        route='<int:question_id>/vote/', 
        view=vote,
        name='vote'
    ),
]
