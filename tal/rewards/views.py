from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
#import MySQLdb
import mysql.connector
from .forms import RecompensaForm
from .models import Recompensa


@method_decorator(login_required, name='dispatch')
class RewardsInicio(TemplateView):
    template_name = "rewards/rewardsInicio.html"

    def get(self, request, *args, **kwargs):
        #db = MySQLdb.connect(user='eguerrero', db='eguerrero$mexa', passwd='Ereslomasbonit0', host='eguerrero.mysql.#pythonanywhere-services.com')
        #cursor = db.cursor()
        #sql = "SELECT SUM(recompensas_recompensa.recompensa), nombreUsuario, recompensas_recompensa.nombreEmpresaUsuario FROM recompensas_recompensa INNER JOIN auth_user ON recompensas_recompensa.nombreEmpresaUsuario  = auth_user.username WHERE recompensas_recompensa.nombreUsuario = '" + str(request.user) + "' and recompensas_recompensa.statusRecompensa = 1 GROUP BY recompensas_recompensa.nombreEmpresaUsuario"
        #print (sql)
        #cursor.execute( sql) #, (str(request.user)))
        #recompensas_recompensa = []
        #for row in cursor.fetchall():
        #    recompensas_recompensa.append(row)
        #db.close()
        miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='toor', db='mexa' )
        cur = miConexion.cursor()
        cur.execute( "SELECT SUM(recompensas_recompensa.recompensa), nombreUsuario, recompensas_recompensa.nombreEmpresaUsuario FROM recompensas_recompensa INNER JOIN auth_user ON recompensas_recompensa.nombreEmpresaUsuario  = auth_user.username WHERE recompensas_recompensa.nombreUsuario = '" + str(request.user) + "' and recompensas_recompensa.statusRecompensa = 1 GROUP BY recompensas_recompensa.nombreEmpresaUsuario" )
        recompensas_recompensa = []
        for row in cur.fetchall() :
            recompensas_recompensa.append(row)
        miConexion.close()
        return render(request, self.template_name, {'recompensas_recompensa': recompensas_recompensa})


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
            #nombreUser = request.POST['nombreUsuario']
            #db = MySQLdb.connect(user='root', db='mexa', passwd='', host='localhost')
            #cursor = db.cursor()
            #sql = "UPDATE recompensas_recompensa SET statusRecompensa = 0 WHERE recompensas_recompensa.nombreUsuario  = '" + nombreUser + "'"
            #cursor.execute( sql)
            #db.close()
            Recompensa.objects.filter(nombreUsuario=request.POST['nombreUsuario']).update(statusRecompensa=0)
            return redirect('/')


        return render(request, 'rewards/delRecompensa.html', {'userName': userName })
    else:
        return redirect('/accounts/login/')

