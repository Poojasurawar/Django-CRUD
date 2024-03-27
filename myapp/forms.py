from django import forms
from myapp.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','mobile','age','city','state','country']
      
from django import forms
from .models import Contact

      
        
        