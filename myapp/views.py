from django.shortcuts import render
from .forms import EjemploForm

def index(request):
    return render(request, 'myapp/index.html')

def formulario(request):
    form = EjemploForm()
    return render(request, 'myapp/form.html', {'form': form})

def dashboard(request):
    return render(request, 'myapp/dashboard.html')




