from django import forms
from .models import Seller, Customer


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'


class CustomerForm(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField()
    date = forms.DateField(widget=forms.SelectDateWidget)
