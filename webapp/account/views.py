from django.shortcuts import render
from django.http import HttpResponse

def account (request):
    return render(request, 'index.html', {'heading': 'Профиль','title': 'Личный кабинет'})

