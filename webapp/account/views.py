from django.shortcuts import render
from django.http import HttpResponse
from .forms import BronForm

def account (request):
    if request.method == "POST":
        form = BronForm(request.POST)
        #if form.is_valid():
        name=request.POST.get("name")
        surname = request.POST.get("surname")
        arrival_date = request.POST.get("arrival_date")
        departure_date = request.POST.get("departure_date")
        adults_count = request.POST.get("adults_count")
        children_count = request.POST.get("children_count")
        pets_count = request.POST.get("pets_count")
        house_count = request.POST.get("house_count")
        return render(request, "account.html", {"form": form, "name": name, "surname": surname, "arrival_date":arrival_date, "departure_date":departure_date, "adults_count":adults_count, "children_count": children_count, "pets_count":pets_count, "house_count":house_count}) 
    else:
        form = BronForm()
    return render(request, "account.html", {"form": form})
    
    
    
    #return render(request, 'account.html', {'heading': 'Профиль','title': 'Личный кабинет'})

