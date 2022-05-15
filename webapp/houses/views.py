from django.shortcuts import render
from django.http import HttpResponse

def houses (request):
    house=["Ванная комната","Кухня","Холодильник","Набор посуды","Подвесное кресло","Две спальные зоны","Wi-Fi"]
    return render(request, 'houses.html', {'house':house,'heading': 'Домики','title': 'Домики'})
