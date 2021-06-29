from django.core import validators
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http.request import validate_host
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 carácteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link', 'nombre', 'apellido', 'birthday', 'telefono', 'calle', 'numero', 'colonia', 'cp']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Tu resumen'}),
            'link': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'@Tu instagram'}),
            'nombre': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Nombre','required': True}),
            'apellido': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Apellido'}),
            'birthday': forms.DateInput(attrs={'class':'form-control mt-3', 'placeholder':'yyyy/mm/dd','required': True }),
            'telefono': forms.NumberInput(attrs={'class':'form-control mt-3', 'placeholder':'Telefono', 'required': True}),
            'calle': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Calle'}),
            'numero': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Numero'}),
            'colonia': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Colonia'}),
            'cp': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'C.P'}),

        }


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 carácteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email