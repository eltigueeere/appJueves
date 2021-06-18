from django import forms

class RecompensaForm(forms.Form):

    recompensa = forms.IntegerField(label="Monto recompensa", required=True)
    nombreUsuario = forms.CharField(label="Nombre Usuario", required=True)
    nombreEmpresa = forms.CharField(label="Empresa que asigna", required=True)


    #class Meta:
    #    model = Recompensa
    #    fields = ['title', 'content', 'order']
    #    widgets = {
    #        'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
    #        'content': forms.Textarea(attrs={'class':'form-control'}),
    #        'order': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Orden  '}),
    #    }
    #    labels = {
    #        'title':'', 'order':'', 'content': ''
    #    }