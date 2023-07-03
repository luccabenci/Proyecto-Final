from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect
from myblog.forms import UserCreationForm, CreateNoteForm, AuthenticationForm, EditarUsuarioForm,RegisterUserForm, NoteListForm
from django.contrib.auth.models import User
from myblog.forms import CreateNote


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        print (form.is_valid())
        if form.is_valid():
            
            user=form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render(request, 'register.html', {'form': form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Usuario o contraseña incorrectos')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu perfil ha sido actualizado.')
            return redirect('editar_perfil')
    else:
        form = EditarUsuarioForm(instance=request.user)

    return render(request, 'editar_perfil.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def change_password(request):
    # Lógica para cambiar la contraseña del usuario
    return render(request, 'change_password.html')

def home(request):
    return render(request, 'home.html')

@login_required
def create_note_view(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = CreateNoteForm()

    return render(request, 'create_note.html', {'form': form})

@login_required
def note_list_view(request):
    if request.method == 'POST':
        form = NoteListForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user  
            note.save()
            title = form.cleaned_data['title']
            return HttpResponseRedirect('home')
    else:
        form = NoteListForm()

    return render(request, 'note_list.html', {'form': form})