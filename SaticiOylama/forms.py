from django import forms
from .models import SaticiOylama
class SaticiOylamaForm(forms.ModelForm):

    oy_puani_f = forms.IntegerField(min_value=1, max_value=10, required=True)

    class Meta:
        model = SaticiOylama
        fields = ("oy_puani_f",)

