from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView
from .forms import QuestionTextForm, ExamForm
from .models import TextQuestion
from django.contrib import messages

# Create your views here.
def create_question_text(request):
    title = "Crie uma questão de Texto"
    if request.method == "POST":
        form = QuestionTextForm(request.POST)
        if form.is_valid():
            form.save()
            print("come here")
            return HttpResponseRedirect(reverse("index"))
        return render(request, 'list/establishment.html', {'form': form,'title':title})

    else:
        form = QuestionTextForm()
        return render(request, 'list/establishment.html', {'form': form,'title':title})


def list_question_text(request):
    question_texts = TextQuestion.objects.all()
    print(question_texts)
    return render(request, 'list/list_question_text.html', {"question_texts": question_texts})

def edit_question_text(request, id):
    title = "Editar Questão Texto"
    question = get_object_or_404(TextQuestion, id=id)
    if request.method == "POST":
        form = QuestionTextForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'list/establishment.html', {'form': form,'title':title})
    else:
        form = QuestionTextForm(instance=question)
        return render(request, 'list/establishment.html', {'form': form,'title':title})

def delete_question_text(request, id):
    delete_question_text = get_object_or_404(TextQuestion, id=id)
    delete_question_text.delete()
    return render(request, 'delete.html')

class NewExamView(FormView):
    template_name = "list/new_exam.html"
    form_class = ExamForm
    success_url = "/"

    def form_valid(self, form):
        form.insert()
        messages.success(self.request, 'Prova criada com sucesso!')
        return super(NewExamView, self).form_valid(form)
