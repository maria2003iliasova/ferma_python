from django import forms
from django.core.exceptions import ValidationError
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
    
    
    #first_name = forms.CharField(max_length=50)
    #last_name = forms.CharField(max_length=50)
    #phone = forms.CharField(max_length=12)

class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = '__all__'
    
    
    
    
    #title = forms.CharField(max_length=50)
    #author = forms.ForeignKey(User, on_delete = models.CASCADE)
    #text = forms.Textarea()
    #photo = forms.ImageField()
    #time_create = forms.DateField()
    #time_update = forms.DateField()
    #is_published = forms.BooleanField()
    
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'
    
    
    
    
    
    #author = forms.ForeignKey(User, on_delete = models.CASCADE)
    #text = forms.Textarea()
    #time_create = forms.DateField()
    #time_update = forms.DateField()
    #articles = forms.ForeignKey(Articles, on_delete = models.CASCADE)

class BronForm(forms.ModelForm):
    class Meta:
        model = Bron
        fields = '__all__'
    
    
    
    
    
    
    #name = forms.CharField(max_length=50, label='Имя')
    #surname = forms.CharField(max_length=50, label='Фамилия')
    #arrival_date = forms.DateField(label='Дата заезда')
    #departure_date = forms.DateField(label='Дата выезда')
    #adults_count = forms.IntegerField(min_value=1 ,label='Сколько взрослых', initial=1)
    #children_count = forms.IntegerField(label='Сколько детей', required=False, initial=0)
    #pets_count = forms.IntegerField(label='Сколько питомцев', required=False, initial=0)
    #info = forms.BooleanField(label='Я ознакомлен с правилами (для тех, кто с питомцами)', required=False)
    #house_count = forms.IntegerField(min_value=1 , label='Сколько домиков', initial=1)
    
    #def clean(self):
    #    super().clean()
    #    pets_count = self.cleaned_data.get('pets_count')
    #    info = self.cleaned_data.get('info')
    #    if pets_count>0:
    #        if info:
    #            pass
    #        else:
    #            raise ValidationError('Вы должны ознокомится с правилами (для тех, кто с питомцами)')