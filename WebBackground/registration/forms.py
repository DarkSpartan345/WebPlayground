from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email=forms.EmailField(required=True,help_text="Obligatorio, debe contener maximo 254 carateres y debe ser valido")
    
    class Meta:
        model=User
        fields=("username","email","password1","password2")
    
    def clean_email(self):
        email=self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este Correo ya ha sido registrado")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=["avatar","bio","link"]
        widgets={
            "avatar":forms.ClearableFileInput(attrs={'class':"form-control-file mt-3"}),
            "bio":forms.Textarea(attrs={"class":"form-control","row":3,"placeholder":"Biografia"}),
            "link":forms.URLInput(attrs={"class":"form-control","placeholder":"Enlace"})
            
        }
class EmailForm(forms.ModelForm):
    email=forms.EmailField(required=True,help_text="Obligatorio, debe contener maximo 254 carateres y debe ser valido")
    class Meta:
         model=User
         fields=["email"]
         
    def clean_email(self):
        email=self.cleaned_data.get("email")
        if "email" in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Este Correo ya ha sido registrado")
            return email
        

