from django.shortcuts import render
from django.http import HttpResponseNotFound

def place (request):
    info={"city":"Владимир", "work":"5 лет"}
    return render(request, 'place.html', {'info':info, 'heading': 'Города','title': 'Где мы находимся'})

def city (request, cityid):
    return render(request, 'city.html', {'city':cityid, 'heading': 'Города','title': 'Где мы находимся'})

def page_not_found_view(request, exception):
    return HttpResponseNotFound("<h2>404 NOT FOUND</h2><p>Страница не найдена</p>")