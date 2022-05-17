from django import forms
from django.core.exceptions import ValidationError

class BronForm(forms.Form):
    name = forms.CharField(max_length=255, label='Имя')
    surname = forms.CharField(max_length=255, label='Фамилия')
    arrival_date = forms.DateField(label='Дата заезда')
    departure_date = forms.DateField(label='Дата выезда')
    adults_count = forms.IntegerField(min_value=1 ,label='Сколько взрослых', initial=1)
    children_count = forms.IntegerField(label='Сколько детей', required=False, initial=0)
    pets_count = forms.IntegerField(label='Сколько питомцев', required=False, initial=0)
    info = forms.BooleanField(label='Я ознакомлен с правилами (для тех, кто с питомцами)', required=False)
    house_count = forms.IntegerField(min_value=1 , label='Сколько домиков', initial=1)
    
    def clean(self):
        super().clean()
        pets_count = self.cleaned_data.get('pets_count')
        info = self.cleaned_data.get('info')
        if pets_count>0:
            if info:
                pass
            else:
                raise ValidationError('Вы должны ознокомится с правилами (для тех, кто с питомцами)')