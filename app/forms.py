from django import forms


class FormSupplier(forms.Form):
    razon = forms.CharField(max_length=100)
    address = forms.EmailField()
    phone = forms.CharField(max_length=10)
    email = forms.CharField(max_length=100)
