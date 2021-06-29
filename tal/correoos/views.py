from django.core.mail import send_mail
from django.http import HttpResponse
#from django.apps import apps
#modelRewards = apps.get_model('app', 'class')
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView, FormView
from django.views.generic.base import TemplateView
from .models import CorreosCumpleInvitacionPublicidad
from .forms import CorreosForm, MailGeneralForm

class CorreosServiciosUpdate(UpdateView):
    form_class = CorreosForm
    success_url = "?ok"
    template_name = 'correoos/inicio_form.html'
    def get_object(self):
        # recuperar el objeto que se va editar
        profileZ, created = CorreosCumpleInvitacionPublicidad.objects.get_or_create(usuarioEmpresa=self.request.user)
        return profileZ

class MandarCorreoGeneralView(FormView):
    template_name = "correoos/mandarCorreo.html"
    form_class = MailGeneralForm
    success_url = '?ok'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        correos = User.objects.values('email')
        correosList = []
        for c in correos:
            correosList.append(c['email'])
        send_mail(subject=self.request.POST['asunto'], message=self.request.POST['cuerpo'], from_email="conjguerrero@gmail.com", recipient_list=correosList,fail_silently=False)
        return super().form_valid(form)



def sendMail(request):
    correos = User.objects.values('email')
    correosList = []
    print(correos)
    for c in correos:
        correosList.append(c['email'])

    print(correosList)

    #send_mail(subject="subject", message="message 11:30", from_email="conjguerrero@gmail.com", recipient_list=correosList,fail_silently=False)

    return HttpResponse("Hello, world. correos.")



def esCumple():
    print()

def invitacion():
    print()

