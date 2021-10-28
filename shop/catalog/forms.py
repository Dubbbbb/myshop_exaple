from django import forms
from .models import *
from django.contrib.auth.models import User

class AddBykeForm(forms.ModelForm):

    class Meta:
        model = Byke
        fields = "__all__"



class AddScooterForm(forms.ModelForm):

    class Meta:
        model = Scooter
        fields = "__all__"

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Вы ввели разные пароли')
        return cd['password2']


    # title = forms.CharField(max_length=255, label="Название")
    # description = forms.CharField(label="Описание", widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    # material_ram = forms.CharField(max_length=100, label="Материал рамы")
    # transmission = forms.IntegerField(label="Количество передач")
    # diameter_wheel = forms.IntegerField(label="Диаметр колес")
    # price = forms.CharField(label="Цена", max_length=100)
    # slug = forms.SlugField(max_length=100, label="URL")
    # category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория")
    # is_published = forms.BooleanField(label="Опубликовано", required=False, initial=True)
