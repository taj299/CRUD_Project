from django import forms
from .models import UserProfile

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name','email','password']
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }