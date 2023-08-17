from django import forms

class RequestForm(forms.Form):
    length = forms.IntegerField()
    symbols = forms.BooleanField(required=False)
    numbers = forms.BooleanField(required=False)