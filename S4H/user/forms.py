from django.forms import ModelForm
from .models import S4HUser, Validation
from .models import GRADE
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class S4HUserForm(forms.Form):
    name = forms.CharField(
        label='Nome:',
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    grade = forms.DecimalField(
        label='Ano/Serie:',
        widget=forms.NumberInput(attrs={'placeholder': ''})
    )
    email = forms.EmailField(
        label='Email:',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

class PasswordForm(S4HUserForm):
    new_password = forms.CharField(
        label='Senha:',
        widget=forms.PasswordInput(attrs={'placeholder': ''})
    )
    renew_password = forms.CharField(
        label='Repita senha:',
        widget=forms.PasswordInput(attrs={'placeholder': ''})
    )

    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)
        self.fields.pop('email')
        self.fields.pop('grade')
        self.fields.pop('name')

    def save(self, user):
        password = self.cleaned_data.get('new_password')
        user.set_password(password)
        user.save()

    def is_password_valid(self, username):
        cleaned_data = super(PasswordForm, self).clean()
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            self.add_error('password', 'Senha incorreta')
            return False
        return True

    def clean(self):
        cleaned_data = super(PasswordForm, self).clean()
        password1 = cleaned_data.get('new_password')
        password2 = cleaned_data.get('renew_password')
        if password1 and password2 and password1 != password2:
            raise ValidationError({'renew_password': 'Senhas nao sao iguais'})

        if len(password1) < 6 or len(password1) > 15:
            raise ValidatioError({'new_password': 'Senha deve conter entre 6 e 15 caracteres'})

class UserForm(S4HUserForm):
    repeat_password = forms.CharField(
        label='Senha:',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': ''})
    )

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop("instance", None)
        editing = kwargs.pop("editing", None)
        super(UserForm, self).__init__(*args, **kwargs)
        if instance is not None:
            self.__dict__["instance"] = instance
        if instance is not None or editing is not None:
            self.fields.pop("password")
            self.fields.pop("repeat_password")

    def set_fields(self, s4h_user):
        s4h_user.name(self.cleaned_data.get('name'))
        s4h_user.user.email = self.cleaned_data.get('email')
        s4h_user.user.username = s4h_user.user.email
        s4h_user.grade = self.cleaned_data.get('grade')

    def update(self, s4h_user):
        self.set_fields(s4h_user)
        try:
            s4h_user.save()
        except:
           raise Exception("Something went wrong so we could not save \
                             your data. Try again later")
        return s4h_user

    def insert(self):
        s4h_user = S4HUser()
        s4h_user.user = User()
        self.set_fields(s4h_user)
        s4h_user.user.set_password(self.cleaned_data.get('password'))
        try:
            s4h_user.save()
        except e:
           raise Exception("Something went wrong so we could not save \
                             your data. Try again later")
        return s4h_user

    def clean_grade(self):
        grade = self.cleaned_data["grade"]
        if (grade > 9 or grade < 1):
            raise ValidationError(['Serie deve ser maior que 1 e menor que 9'])
        return grade

    def clean_email(self):
        email = self.cleaned_data["email"]
        if hasattr(self,"instance") and self.instance.user.email == email:
            return email
        elif User.objects.filter(email=email).exists():
                raise ValidationError('Email already used.')

        return email

    def clean_name(self):
        validation = Validation()
        name = self.cleaned_data['name']

        if (len(name) < 2 or len(name) > 50):
            raise ValidationError(['Name must be between 2 and \
                                               50 characters.', ])

        if validation.hasSpecialCharacters(name):
            raise ValidationError(['Name cannot contain special \
                                               characters.', ])

        if validation.hasNumbers(name):
            raise ValidationError(['Name cannot contain numbers.', ])
        return name

    def clean(self):
        cleaned_data = super(UserForm, self).clean()

        if "password" in self.fields and "repeat_password" in self.fields:
            password1 = cleaned_data['password']
            password2 = cleaned_data['repeat_password']

            if len(password1) < 6 or len(password1) > 15:
                raise ValidationError({'password': ['Password must be \
                                                       between 6 and 15 \
                                                       characters.', ]})

            if password1 and password2 and password1 != password2:
                raise ValidationError({'repeat_password': ['Passwords do \
                                                              not match.', ]})
        return cleaned_data
