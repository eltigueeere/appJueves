from django.urls import path
from .views import DeliberryInicio
urlpatterns = [
    path('', DeliberryInicio.as_view(), name="deliberry"),
]