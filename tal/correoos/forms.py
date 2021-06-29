from correoos.models import CorreosCumpleInvitacionPublicidad
from django import forms

class CorreosForm(forms.ModelForm):
    class Meta:
        model = CorreosCumpleInvitacionPublicidad
        fields = ['usuarioEmpresa', 'esCumple','invitacion']
        widgets = {
            'usuarioEmpresa': forms.TextInput(attrs={'class':'form-control mt-3', 'type': 'hidden', 'placeholder':'Empresa'}),
            'esCumple': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Si/No'}),
            'invitacion': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Si/No'}),
        }

class MailGeneralForm(forms.Form):
    fields = ['asunto', 'cuerpo']
    widgets ={
        'asunto': forms.TextInput(),
        'cuerpo': forms.Textarea(),
    }