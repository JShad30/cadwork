from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    """Form to be used to log the users in"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class UserRegistrationForm(UserCreationForm):
    """Form used to register a new user"""
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'A user has already been created with that email address')
        return email
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise ValidationError('Please confirm your password')
            
        if password1 != password2:
            raise ValidationError('Your passwords do not match')
            
        return password2
        

class ConfirmPasswordResetForm(forms.Form):
    """Form for the user to fill out new password"""
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
