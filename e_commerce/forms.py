from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class ContactForm(forms.Form):
    name = forms.CharField(
        error_messages={'required':'Mandatory name insert.'},
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Type your name"
            }
        )
    )
    email = forms.EmailField(
        error_messages={'invalid':'Type a valid email.'},
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Type your e-mail"
            }
        )
    )
    message = forms.CharField(
        error_messages={'required':'Mandatory text insert.'},
        widget=forms.Textarea(
            attrs={
                "class":"form-control",
                "placeholder":"Type your text"
            }
        )
    )


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

def clean_username(self):
       username = self.cleaned_data.get("username") 
       qs = User.objects.filter(username=username)
       if qs.exists():
           raise forms.ValidationError("This username alreagy exist. Choose another")

       return username

def clean_email(self):
       email = self.cleaned_data.get("email") 
       qs = User.objects.filter(email=email)
       if qs.exists():
           raise forms.ValidationError("This email alreagy exist. Choose another")

       return email