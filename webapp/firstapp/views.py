from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def home (request):
    return render(request, 'index.html', {'heading': 'Ферма в лесу','title': 'Главная страница'})

def page_not_found_view(request, exception):
    return HttpResponseNotFound("<h2>404 NOT FOUND</h2><p>Страница не найдена</p>")
    