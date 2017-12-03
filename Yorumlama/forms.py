from  django import forms
from .models import UrunYorumlama
class UrunYorumlamaForms(forms.ModelForm):

    yorum_baslik_f = forms.CharField(required=True, max_length=30)
    yorum_icerik_f = forms.CharField(required=True, widget=forms.Textarea)

    class Meta:
        fields = ("yorum_baslik_f", "yorum_icerik_f")
        model = UrunYorumlama
