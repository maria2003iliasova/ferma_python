from django.shortcuts import render
from django.http import HttpResponse

def place (request):
    return render(request, 'index.html', {'heading': 'Города','title': 'Где мы находимся'})

def city (request, cityid):
    return render(request, 'city.html', {'city':cityid, 'heading': 'Города','title': 'Где мы находимся'})
