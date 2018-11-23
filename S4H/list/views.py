from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .forms import QuestionTextForm, ExerciseForm
from .models import TextQuestion, Exercise

# Create your views here.
def create_question_text(request):
    title = "Crie uma questão de Texto"
    if request.method == "POST":
        form = QuestionTextForm(request.POST)
        if form.is_valid():
            form.save()
            print("come here")
            return HttpResponseRedirect(reverse("index"))
        return render(request, 'establishment.html', {'form': form,'title':title})

    else:
        form = QuestionTextForm()
        return render(request, 'establishment.html', {'form': form,'title':title})


def create_exercise(request):
    title = "Crie um exercicio"
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            print("come here")
            return HttpResponseRedirect(reverse("index"))
        return render(request, 'establishment.html', {'form': form,'title':title})

    else:
        form = ExerciseForm()
        return render(request, 'establishment.html', {'form': form,'title':title})


def list_question_text(request):
    question_texts = TextQuestion.objects.all()
    print(question_texts)
    return render(request, 'list_question_text.html', {"question_texts": question_texts})

def list_exercise(request):
    lista = []
    exercises1 = Exercise.objects.first()
    exercises = exercises1.question.first()
    print(lista)

    print(exercises)
    return render(request, 'list_exercises.html', {"exercises": exercises})

def edit_question_text(request, id):
    title = "Editar Questão Texto"
    question = get_object_or_404(TextQuestion, id=id)
    if request.method == "POST":
        form = QuestionTextForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'establishment.html', {'form': form,'title':title})
    else:
        form = QuestionTextForm(instance=question)
        return render(request, 'establishment.html', {'form': form,'title':title})

def delete_question_text(request, id):
    delete_question_text = get_object_or_404(TextQuestion, id=id)
    delete_question_text.delete()
    return render(request, 'delete.html')
