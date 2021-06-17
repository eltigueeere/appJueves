from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class RewardsInicio(TemplateView):
    template_name = "rewards/rewardsInicio.html"