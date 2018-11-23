from .models import TextQuestion
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
        

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