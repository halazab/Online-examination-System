from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import QuestionsForm
from django.http import HttpResponse
def add_question(request):
    form = QuestionsForm
    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            HttpResponse("Form is Invalid")
    return render(request, 'question/create_question.html', {'form': form})