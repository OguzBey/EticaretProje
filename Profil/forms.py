from django import forms
from Uyelik.models import MyUser
from django.contrib.auth.models import User
from django.forms import ValidationError
class UserEditForm(forms.ModelForm):

    email = forms.EmailField(required=True, help_text='Email Adresinizi giriniz..')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')



class MyUserEditForm(forms.ModelForm):
    ACCEPTABLE_FORMATS = ['%d/%m/%Y']  # 01-01-2011
    adres = forms.CharField(max_length=100, widget=forms.Textarea, required=False)
    dogum_tarihi = forms.DateField(input_formats=ACCEPTABLE_FORMATS, required=False)
    profil_fotosu = forms.ImageField(required=False)

    class Meta:
        model = MyUser
        fields = ('adres', 'dogum_tarihi', 'profil_fotosu')


