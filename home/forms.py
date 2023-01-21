from django import forms
from home.models import Sold_prduct
class soldProductForm(forms.ModelForm):
    class Meta:
        model=Sold_prduct
        fields= ['product', 'qty']