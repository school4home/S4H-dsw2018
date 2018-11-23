from .models import TextQuestion
from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Exam, ExamQuestion
from school.models import SchoolYear

REPETITIONS = 3

class QuestionTextForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuestionTextForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Enviar'))

    class Meta:
        model = TextQuestion
        fields = '__all__'
        labels = {
            'name': 'Autor',
      #      'start_date': 'Data da Elaboracao da Questao',
            'description': 'Descrição',
            'text_question': 'Questão'
        }

class ExamForm(forms.Form):

    application_date = forms.DateField(
        label='Data da Prova:',
        required=True,
        widget=forms.SelectDateWidget()
    )
    school_year = forms.DecimalField(
        label='Série',
        required=True,
        widget=forms.NumberInput()
    )

    def __init__(self, *args, **kwargs):
        super(ExamForm, self).__init__(*args, **kwargs)
        for count in range(REPETITIONS):
            self.fields['question_%d' % (count + 1)] = forms.CharField(
            label=('Questão %d:' % (count + 1)),
            required=True,
            widget=forms.Textarea
            )
            self.fields['answer_question_%d' % (count + 1)] = forms.CharField(
            label=('Resposta:'),
            required=True,
            widget=forms.Textarea
            )

    def set_exam(self, exam):
        exam.application_date = self.cleaned_data.get('application_date')
        exam.school_year = SchoolYear.get_instance(self.cleaned_data.get('school_year'))
        return exam

    def set_questions(self, exam):
        questions = []
        for count in range(REPETITIONS):
            questions.append(ExamQuestion())
            questions[count].question_text = self.cleaned_data.get('question_%d' % (count + 1))
            questions[count].correct_answer = self.cleaned_data.get('answer_question_%d' % (count + 1))
            questions[count].exam = exam
        return questions

    def insert(self):
        exam = Exam()
        exam = self.set_exam(exam)
        questions = self.set_questions(exam)
        try:
            exam.save()
            for question in questions:
                question.save()
        except Exception as e:
            print(e)

    def clean(self):
        self.cleaned_data = super(ExamForm, self).clean()
