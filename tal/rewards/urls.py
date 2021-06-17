from django.urls import path
from .views import RewardsInicio
urlpatterns = [
    path('', RewardsInicio.as_view(), name="rewards"),
]