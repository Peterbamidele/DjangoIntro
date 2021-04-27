from django.shortcuts import render

# Create your views here.
from .models import Question, Choice


def index(request):
    questions = Question.objects.all()
    context = {"questions": questions}
    return render(request, 'Poll/index.html', context)
