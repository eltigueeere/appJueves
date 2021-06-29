from django.shortcuts import render
from django.views.generic.base import TemplateView

class DeliberryInicio(TemplateView):
    template_name = "deliberry/menu.html"