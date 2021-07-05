from django.shortcuts import render
from django.views.generic.edit import FormView
from .form import PedidoForm
from .models import PedidoEnTienda
from datetime import datetime
from django.views.generic.list import ListView


class PedidosEnTiendaListView(ListView):


    #template_name = 'deliberry/pedidoTienda_list.html'
    model = PedidoEnTienda
    paginate_by = 100 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context





class DeliberryInicio(FormView):
    template_name = 'deliberry/menu.html'
    form_class = PedidoForm
    success_url = '?ok'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        ordenes=[]
        try:
            if self.request.POST['confimar1'] == 'on':
                ordenes.append(str(self.request.POST['cantidad1']) + " orden's de "+ str(self.request.POST['orden1Input']) + " con " + str(self.request.POST['extra1']))

            if self.request.POST['confimar2'] == 'on':
                ordenes.append(str(self.request.POST['cantidad1']) + " orden's de "+ str(self.request.POST['orden2Input']) + " con " + str(self.request.POST['extra2']))
        except:
            print("No se confirmo alguna orden.")
        finally:
            PedidoEnTienda(usuario=str(self.request.user), fechaDeOrden=datetime.now(), pedido= ordenes).save()
        return super().form_valid(form)