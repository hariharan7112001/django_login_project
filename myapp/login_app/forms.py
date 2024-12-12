from django import forms
from .models import SignUp
import re

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['user_name', 'email', 'password_one', 'password_two']

    def clean(self):
        cleaned_data = super().clean()
        password_one = cleaned_data.get('password_one')
        password_two = cleaned_data.get('password_two')
        if len(password_one) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        if not re.search(r"[A-Z]", password_one):
            raise forms.ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r"[0-9]", password_one):
            raise forms.ValidationError("Password must contain at least one digit.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password_one):
            raise forms.ValidationError("Password must contain at least one special character.")


        if password_one and password_two and password_one != password_two:
            raise forms.ValidationError("Passwords do not match!")  
        return cleaned_data
