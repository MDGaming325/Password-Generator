from django import forms


class RequestForm(forms.Form):
    length = forms.IntegerField(min_value=1, initial=16)
    symbols = forms.BooleanField(required=False, initial=True)
    numbers = forms.BooleanField(required=False, initial=True)
