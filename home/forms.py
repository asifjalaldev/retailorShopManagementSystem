from django import forms
from home.models import Product,Easypaisa_out
# class searchForm(forms.ModelForm):
#     class Meta:
#         fields=['date']
class easypaisaOutForm(forms.ModelForm):
    class Meta:
        model=Easypaisa_out
        fields=['easypaisa_balance_out', 'charges']