from django import forms
from .models import Urun

class UrunEkleForm(forms.ModelForm):

    urun_adi_f = forms.CharField(max_length=40, required=True, label="Ürün Adı")
    urun_resmi_f = forms.ImageField(required=False, label="Ürün Resmi")
    urun_stok_f = forms.IntegerField(required=True, label="Stok")
    urun_fiyati_f = forms.FloatField(required=True, label="Fiyatı")
    urun_aciklama_f = forms.CharField(required=False, widget=forms.Textarea, label="Açıklama")

    class Meta:
        model = Urun
        fields = ('urun_adi_f', 'urun_resmi_f', 'urun_stok_f', 'urun_fiyati_f', 'urun_aciklama_f')