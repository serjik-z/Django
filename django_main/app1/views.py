from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123']
    }
    return render(request, 'django_main/index.html', data)
def index1(request):
    return render(request, 'django_main/index1.html')