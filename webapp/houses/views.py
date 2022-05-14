from django.shortcuts import render
from django.http import HttpResponse

def houses (request):
    return render(request, 'index.html', {'heading': 'Домики','title': 'Домики'})
