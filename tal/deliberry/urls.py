from django.urls import path
from .views import DeliberryInicio, PedidosEnTiendaListView
urlpatterns = [
    path('', DeliberryInicio.as_view(), name="deliberry"),
    path('pedidosEnTienda/', PedidosEnTiendaListView.as_view(), name='pedidosEnTienda'),
]