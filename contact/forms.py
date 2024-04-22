from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    """Subscription form"""
    class Meta:
        model = Contact
        fields = ("email", )
        widgets = {
            "email": forms.TextInput(attrs={"class": "editContent", "placeholder": "Email..."})
        }
        labels ={
            "email": ''
        }