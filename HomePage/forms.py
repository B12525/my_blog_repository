from django import forms
from .models import UserInfo

class FormUser(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['your_name','your_email','your_password']
