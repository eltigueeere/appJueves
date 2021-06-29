from django.urls import path
from .views import RewardsInicio
from . import views

urlpatterns = [
    path('', RewardsInicio.as_view(), name="rewards"),
    path('compra/<userName>/', views.compraUsuario, name='compra'),
    path('delRecompensas/<userName>/', views.delRecompensa, name='delRecompensas'),
]