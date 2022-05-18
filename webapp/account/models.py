from multiprocessing import AuthenticationError
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    
class Bron(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    adults_count = models.IntegerField()
    children_count = models.IntegerField()
    pets_count = models.IntegerField()
    info = models.BooleanField()
    house_count = models.IntegerField()

class Articles(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    photo = models.ImageField()
    time_create = models.DateField()
    time_update = models.DateField()
    is_published = models.BooleanField()
    
class Comments(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    time_create = models.DateField()
    time_update = models.DateField()
    articles = models.ForeignKey(Articles, on_delete = models.CASCADE)
