from django import forms


# Create your forms here.


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=50)

    sender = forms.EmailField(max_length=150)
    subject = forms.CharField(max_length=500)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
