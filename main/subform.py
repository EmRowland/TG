from django import forms


class SubForm(forms.Form):
    sender = forms.EmailField(max_length=150)
