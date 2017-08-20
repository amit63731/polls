from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.shortcuts import render
from django.http import Http404



def index(request):
	latest_question_list = Question.objects.order_by('pub_date')
	output = [p.question_text for p in latest_question_list]
	template  = "polls/index.html"
	context = {'latest_question_list' : latest_question_list}
	return render(request, template, context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})