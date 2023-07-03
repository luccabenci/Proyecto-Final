from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.db import models
from blog.models import CreateNote


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    username= forms.CharField(label="Nombre de Usuario")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EditarUsuarioForm (forms.Form):
    email = forms.EmailField(required =False)
    first_name = forms.CharField(label='Nombre', max_length=30, required=False)
    last_name = forms.CharField(label='Apellido', max_length=30, required=False)
    avatar = forms.ImageField (required=False)

class login_requestAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = CreateNote
        fields = ['user', 'title', 'content', 'image']

class NoteListForm(forms.Form):
    # Campos del formulario
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    created_at = forms.DateTimeField()
    image = forms.ImageField(required=False)