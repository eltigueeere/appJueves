from django import forms

class PedidoForm(forms.Form):
    orden1Input = forms.CharField()
    extra1 = forms.Textarea()
    cantidad1 = forms.IntegerField()
    confimar1 = forms.CheckboxInput()

    orden2Input = forms.CharField()
    extra2 = forms.Textarea()
    cantidad2 = forms.IntegerField()
    confimar2 = forms.CheckboxInput()

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass