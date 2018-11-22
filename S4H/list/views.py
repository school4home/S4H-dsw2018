from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .forms import QuestionTextForm

# Create your views here.
def create_question_text(request):
    title = "Crie uma questão"
    if request.method == "POST":
        form = QuestionTextForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        return render(request, 'question_text.html', {'form': form,'title':title})

    else:
        form = QuestionTextForm()
        return render(request, 'question_text.html', {'form': form,'title':title})