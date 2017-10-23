import email
from django import forms
from .models import MyUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget
import  datetime
class UserForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Email Adresinizi giriniz..')
    MUSTERI = "MS"
    SATICI = "ST"
    SECENEKLER = (
        (MUSTERI, "Müşteri"),
        (SATICI, "Satıcı"),
    )

    ACCEPTABLE_FORMATS = ['%d/%m/%Y']  # 01-01-2011
    kullanici_tipi = forms.ChoiceField(required=True, choices=SECENEKLER)
    adres = forms.CharField(max_length=100, widget=forms.Textarea, required=False)
    dogum_tarihi = forms.DateField(input_formats=ACCEPTABLE_FORMATS, required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',
                  'kullanici_tipi', 'adres', 'dogum_tarihi')

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")

        user = super(UserForm, self).save(commit=True)

        user_profile = MyUser(user=user, kullanici_tipi=self.cleaned_data['kullanici_tipi'],
                                   adres=self.cleaned_data['adres'],
                              dogum_tarihi=self.cleaned_data['dogum_tarihi'])
        user_profile.save()
        return user
