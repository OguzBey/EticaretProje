import email
from django import forms
from Uyelik.models import MyUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.files import File
import os
from marketle import settings
from PIL import Image
class UserEditForm(forms.ModelForm):

    email = forms.EmailField(required=True, help_text='Email Adresinizi giriniz..')
    # ACCEPTABLE_FORMATS = ['%d/%m/%Y']  # 01-01-2011
    # adres = forms.CharField(max_length=100, widget=forms.Textarea, required=False)
    # dogum_tarihi = forms.DateField(input_formats=ACCEPTABLE_FORMATS, required=False)
    # profil_fotosu = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

    # def save(self, commit=True):
    #     if not commit:
    #         raise NotImplementedError("Kayıt hatası")
    #
    #     user = super(UserEditForm, self).save(commit=True)
    #
    #     return user
class MyUserEditForm(forms.ModelForm):
    ACCEPTABLE_FORMATS = ['%d/%m/%Y']  # 01-01-2011
    adres = forms.CharField(max_length=100, widget=forms.Textarea, required=False)
    dogum_tarihi = forms.DateField(input_formats=ACCEPTABLE_FORMATS, required=False)
    profil_fotosu = forms.ImageField(required=False)

    class Meta:
        model = MyUser
        fields = ('adres', 'dogum_tarihi', 'profil_fotosu')

    # def save (self, commit=True ):
    #
    #     user_profile = super(MyUserEditForm, self).save(commit)
    #     # user_profile.save()
    #     return user_profile
