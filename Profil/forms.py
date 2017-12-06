from django import forms
from Uyelik.models import MyUser
from django.contrib.auth.models import User
from django.core.validators import validate_email

class UserEditForm(forms.ModelForm):

    email = forms.EmailField(required=True, help_text='Email Adresinizi giriniz..', disabled=True)
    username = forms.CharField(required=True, help_text='Username', disabled=True)


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


class HesapAyarlariForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     username = self.cleaned_data.get('username')
    #     if email and User.objects.filter(email=email).exclude(username=username).exists():
    #         raise forms.ValidationError(u'Böyle bir email adresi zaten var.')
    #     return email

    def __init__(self, *args, **kwargs):
        self.req = kwargs.pop("request", None)
        super(HesapAyarlariForm, self).__init__(*args, **kwargs)
        self.user = self.instance

        if self.instance:
            if self.req.method == "GET":
                self.initial['username'] = self.instance.username
                self.initial['email'] = self.instance.email
                self.initial['password'] = ""


    def clean(self):
        cleaned_data = super(HesapAyarlariForm, self).clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if username:
            if self.user.username != username and User.objects.filter(username=username).exists():
                raise forms.ValidationError("Böyle bir kullanıcı adı zaten var..")
        else:
            raise forms.ValidationError("Lütfen geçerli bir kullanıcı adı girin..")
        if email:
            if self.user.email != email and User.objects.filter(email=email).exists():
                raise forms.ValidationError("Böyle bir email zaten var..")
        else:
            raise forms.ValidationError("Lütfen geçerli bir email adresi girin..")
        if password:
            if not self.user.check_password(password):
                raise forms.ValidationError("Lütfen parolanızı doğru giriniz..")
        else:
            raise forms.ValidationError("Parolanızı girin..")





