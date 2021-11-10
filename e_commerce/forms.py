from django import forms

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

    def clean_email(self):
       email = self.cleaned_data.get("email") 
       if not "gmail.com" in email:
           raise forms.ValidationError("Mail must be gmail.com")

       return email