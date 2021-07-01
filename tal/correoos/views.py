from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView, FormView
from django.shortcuts import render, redirect
from .models import CorreosCumpleInvitacionPublicidad
from .forms import CorreosForm, MailGeneralForm
from django.apps import apps
import pywhatkit as pw

perfil = apps.get_model('registration', 'Profile')


class CorreosServiciosUpdate(UpdateView):
    form_class = CorreosForm
    success_url = "?ok"
    template_name = 'correoos/inicio_form.html'
    def get_object(self):
        # recuperar el objeto que se va editar
        profileZ, created = CorreosCumpleInvitacionPublicidad.objects.get_or_create(usuarioEmpresa=self.request.user)
        return profileZ


@method_decorator(login_required, name='dispatch')
class MandarCorreoGeneralView(FormView):
        template_name = "correoos/mandarCorreo.html"
        form_class = MailGeneralForm
        success_url = '?ok'

        def form_valid(self, form, request):            
            if (request.user.is_authenticated and ( request.user.groups.filter(name='empresa').exists() or request.user.is_staff )):
                # This method is called when valid form data has been POSTed.
                # It should return an HttpResponse.
                correos = User.objects.values('email')
                correosList = []
                for c in correos:
                    correosList.append(c['email'])
                send_mail(subject=self.request.POST['asunto'], message=self.request.POST['cuerpo'], from_email="conjguerrero@gmail.com", recipient_list=correosList,fail_silently=False)
                return super().form_valid(form)

            else:

                return redirect('/accounts/login/')


def sendMail(request):

    if (request.user.is_authenticated and (request.user.groups.filter(name='empresa').exists() or request.user.is_staff )):

        esCumple()
    else:

        return redirect('/accounts/login/')

    return HttpResponse("Hello, world. correos.")



def esCumple():
    x = datetime.now()
    dia = x.strftime("%d")
    mes = x.strftime("%m")
    cumpleaneros=[]
    correosList=[]
    aFelicitar = perfil.objects.all()
    for af in aFelicitar:
        if af.birthday != None:
            cumpleSplit = af.birthday.split("/")
            if dia == cumpleSplit[2] and mes == cumpleSplit[1]:
                cumpleaneros.append(af.user_id)
    
    print(cumpleaneros) 
            
    for i in cumpleaneros:
        correos = User.objects.values('id', 'username', 'email').filter(id=i)
        correosList.append(correos[0]['email'])
        print (correosList)
        send_mail(subject="Feliz cumpleaños " + correos[0]['username'], message="Queremos que disfrutes tu cumpleaños con nosotros ven te espera una sorpresa.", from_email="conjguerrero@gmail.com", recipient_list=correosList,fail_silently=False)
        correosList=[]





class WhatsAppEmail(TemplateView):

    template_name = "correoos/elWha.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context