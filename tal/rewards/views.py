from django.shortcuts import render
from django.db.models import Sum
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RecompensaForm
from .models import Recompensa


@method_decorator(login_required, name='dispatch')
class RewardsInicio(TemplateView):
    template_name = "rewards/rewardsInicio.html"
    template_name2 = "rewards/rewardsInicio2.html"
    def get(self, request, *args, **kwargs):
        recompensas_recompensa=0
        recompensas_recompensa_empresa=0
        if (request.user.is_authenticated and (request.user.groups.filter(name='empresa').exists() or request.user.is_staff )):
            recompensas_recompensa_empresa = Recompensa.objects.values('nombreUsuario').filter(statusRecompensa=1).order_by('nombreUsuario').annotate(total_recompensa=Sum('recompensa'))
            return render(request, self.template_name2, {'saludo': 'Hola', 'usuario':self.request.user ,  'recompensas_recompensa_empresa': recompensas_recompensa_empresa,})
        else:
            recompensaUser = Recompensa.objects.all().filter(nombreUsuario=self.request.user, statusRecompensa=1)
            for rc in recompensaUser:
                recompensas_recompensa = recompensas_recompensa + rc.recompensa
            return render(request, self.template_name, {'saludo': 'Hola', 'usuario':self.request.user ,  'recompensas_recompensa': recompensas_recompensa,})


def compraUsuario(request, userName):
    if (request.user.is_authenticated and (request.user.groups.filter(name='empresa').exists() or request.user.is_staff )):
        form_1 = RecompensaForm()
        if request.method == "POST":
            form_1 = RecompensaForm(data=request.POST)
            print(request.POST)
            if form_1.is_valid():
                recompensa = request.POST.get('recompensa', '')
                nombreUsuario = request.POST.get('nombreUsuario', '')
                nombreEmpresaUsuario = request.POST.get('nombreEmpresaUsuario', '')
                producto = request.POST.get('producto', '')
                recompensaSave=Recompensa(recompensa=recompensa, nombreUsuario=nombreUsuario, nombreEmpresaUsuario=nombreEmpresaUsuario, producto=producto, fechaCompra=datetime.now(), statusRecompensa=1)
                recompensaSave.save()
                return redirect('/')

            recompensaSave=Recompensa(recompensa=request.POST['recompensa'], nombreUsuario=request.POST['nombreUsuario'], nombreEmpresaUsuario=request.POST['nombreEmpresaUsuario'], producto=request.POST['producto'], fechaCompra=datetime.now(), statusRecompensa=1)
            print(recompensaSave)
            recompensaSave.save()
            return redirect('/')

        return render(request, 'rewards/recompensasAdd.html', {'userName': userName })
    else:
        return redirect('/accounts/login/')



def delRecompensa(request, userName):
    if (request.user.is_authenticated and (request.user.groups.filter(name='empresa').exists() or request.user.is_staff )):

        if request.method == "POST":
            Recompensa.objects.filter(nombreUsuario=request.POST['nombreUsuario']).update(statusRecompensa=0)
            return redirect('/')


        return render(request, 'rewards/delRecompensa.html', {'userName': userName })
    else:
        return redirect('/accounts/login/')

