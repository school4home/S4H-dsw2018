from .models import TextQuestion, Exercise
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

class ExerciseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExerciseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Enviar'))

    class Meta:
        model = Exercise
        fields = '__all__'
        labels = {
            'name': 'Autor',
      #      'start_date': 'Data da Elaboracao da Questao',
            'description': 'Descrição',
            'question': 'Questões'
        } 
"""
class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__'
        labels = {
            'name': 'Autor',
      #      'start_date': 'Data da Elaboracao da Questao',
            'description': 'Descrição',
            'text_question': 'Questões'
        } 

    # Representing the many to many related field in Pizza
    #toppings = forms.ModelMultipleChoiceField(queryset=Topping.objects.all())
    toppings = forms.ModelMultipleChoiceField(queryset=Exercise.objects.all())

    # Overriding __init__ here allows us to provide initial
    # data for 'toppings' field
    def __init__(self, *args, **kwargs):
        # Only in case we build the form from an instance
        # (otherwise, 'toppings' list should be empty)
        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.                
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            initial['toppings'] = [t.pk for t in kwargs['instance'].topping_set.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

    # Overriding save allows us to process the value of 'toppings' field    
    def save(self, commit=True):
        # Get the unsave Pizza instance
        instance = forms.ModelForm.save(self, False)

        # Prepare a 'save_m2m' method for the form,
        old_save_m2m = self.save_m2m
        def save_m2m():
           old_save_m2m()
           # This is where we actually link the pizza with toppings
           instance.topping_set.clear()
           instance.topping_set.add(*self.cleaned_data['toppings'])
        self.save_m2m = save_m2m

        # Do we need to save all changes now?
        if commit:
            instance.save()
            self.save_m2m()

        return instance
        """