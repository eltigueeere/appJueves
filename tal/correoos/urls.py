from django.urls import path
from . import views
from .views import CorreosServiciosUpdate, MandarCorreoGeneralView, WhatsAppEmail

urlpatterns = [
    path('', CorreosServiciosUpdate.as_view(), name='CorreosServiciosUpdate'),
    path('sendMail', views.sendMail, name='sendMail'),
    path('sendMailGeneral', MandarCorreoGeneralView.as_view(), name='sendMailGeneral'),
    path('whatsAppEmail', WhatsAppEmail.as_view(), name='whatsAppEmail'),
]
