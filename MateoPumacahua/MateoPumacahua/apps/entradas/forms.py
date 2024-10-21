from django import forms
from .models import Alumno, Profesor
from django.contrib.auth.forms import AuthenticationForm

class AlumnoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Alumno
        fields = '__all__'

class ProfesorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profesor
        fields = '__all__'


class EmailAuthenticationForm(AuthenticationForm):
    correo = forms.EmailField(label='Correo electrónico')