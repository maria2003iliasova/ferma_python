from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .forms import *

def account (request):
    return render(request, 'account.html', {'heading': 'Создание','title': 'Создание'})

#Создание пользователя
def createUser (request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create(**form.cleaned_data)
    else:
        form = UserForm()
    user = User.objects.all()
    return render(request, "createUser.html", {"form": form, "user":user})

#Редактирование пользователя
def editUser(request, id):
    try:
        user = User.objects.get(id=id)
        if request.method == "POST":
            form = UserForm()
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.phone = request.POST.get("phone")
            user.save()
            return HttpResponseRedirect("/")
        else:
            form = UserForm() 
            return render(request, "editUser.html", {"form": form, "user":user})
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>User not found</h2>")

#Удаление пользователя
def deleteUser(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return HttpResponseRedirect("/")
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>Bron not found</h2>")








#Бронирование (создание и вывод)    
def createBron (request):
    if request.method == "POST":
        form = BronForm(request.POST)
        if form.is_valid():
            Bron.objects.create(**form.cleaned_data)
    else:
        form = BronForm()
    bron = Bron.objects.all()
    return render(request, "createBron.html", {"form": form, "bron":bron})    

#Редактирование бронирования
def editBron(request, id):
    try:
        bron = Bron.objects.get(id=id)
        if request.method == "POST":
            form = BronForm()
            bron.arrival_date = request.POST.get("arrival_date")
            bron.departure_date = request.POST.get("departure_date")
            bron.adults_count = request.POST.get("adults_count")
            bron.children_count = request.POST.get("children_count")
            bron.pets_count = request.POST.get("pets_count")
            bron.info = request.POST.get("info")=="on"
            bron.house_count = request.POST.get("house_count")
            bron.save()
            return HttpResponseRedirect("/")
        else:
            form = BronForm() 
            return render(request, "editBron.html", {"form": form, "bron": bron})
    except Bron.DoesNotExist:
        return HttpResponseNotFound("<h2>Bron not found</h2>")

#Удаление бронирования
def deleteBron(request, id):
    try:
        bron = Bron.objects.get(id=id)
        bron.delete()
        return HttpResponseRedirect("/")
    except Bron.DoesNotExist:
        return HttpResponseNotFound("<h2>Bron not found</h2>")    
    
    
    



    
    
#Создание статьи
def createArticles (request):
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            Articles.objects.create(**form.cleaned_data)
    else:
        form = ArticlesForm()
    articles = Articles.objects.all()
    return render(request, "createArticles.html", {"form": form, "articles":articles})

#Редактирование статьи
def editArticles(request, id):
    try:
        articles = Articles.objects.get(id=id)
        if request.method == "POST":
            form = ArticlesForm()
            articles.title = request.POST.get("title")
            articles.text = request.POST.get("text")
            articles.time_create = request.POST.get("time_create")
            articles.time_update = request.POST.get("time_update")
            articles.is_published = request.POST.get("is_published")=="on"
            articles.save()
            return HttpResponseRedirect("/")
        else:
            form = ArticlesForm() 
            return render(request, "editArticles.html", {"form": form, "articles":articles})
    except Articles.DoesNotExist:
        return HttpResponseNotFound("<h2>Articles not found</h2>")

#Удаление статьи
def deleteArticles(request, id):
    try:
        articles = Articles.objects.get(id=id)
        articles.delete()
        return HttpResponseRedirect("/")
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>Frticles not found</h2>")
    
    
    
    
    
    
    
    


#Создание комментария
def createComments (request):
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            Comments.objects.create(**form.cleaned_data)
        else: print("dsgfhj")
    else:
        form = CommentsForm()
    coms = Comments.objects.all()
    return render(request, "createComments.html", {"form": form, "сoms":coms})

#Редактирование комментария
def editComments(request, id):
    try:
        сomments = Comments.objects.get(id=id)
        if request.method == "POST":
            form = CommentsForm()
            сomments.articles = request.POST.get("articles")
            сomments.text = request.POST.get("text")
            сomments.time_create = request.POST.get("time_create")
            сomments.time_update = request.POST.get("time_update")
            сomments.save()
            return HttpResponseRedirect("/")
        else:
            form = CommentsForm() 
            return render(request, "editComments.html", {"form": form, "articles":сomments})
    except Comments.DoesNotExist:
        return HttpResponseNotFound("<h2>Comments not found</h2>")

#Удаление комментария
def deleteComments(request, id):
    try:
        articles = Comments.objects.get(id=id)
        articles.delete()
        return HttpResponseRedirect("/")
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>Comments not found</h2>")













    
    #if request.method == "POST":
    #    form = BronForm(request.POST)
        #if form.is_valid():
    #    name=request.POST.get("name")
    #    surname = request.POST.get("surname")
    #    arrival_date = request.POST.get("arrival_date")
    #    departure_date = request.POST.get("departure_date")
    #    adults_count = request.POST.get("adults_count")
    #    children_count = request.POST.get("children_count")
    #    pets_count = request.POST.get("pets_count")
    #    info = request.POST.get("info")
    #    house_count = request.POST.get("house_count")
    #    return render(request, "account.html", {"form": form, "name": name, "surname": surname, "arrival_date":arrival_date, "departure_date":departure_date, "adults_count":adults_count, "children_count": children_count, "pets_count":pets_count, "info":info, "house_count":house_count}) 
    #else:
    #    form = BronForm()
    #return render(request, "account.html", {"form": form})
    
    
    
    #return render(request, 'account.html', {'heading': 'Профиль','title': 'Личный кабинет'})

