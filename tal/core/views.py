from datetime import timedelta
from datetime import datetime
from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':"Para ser un socio de esta APP contactanos."})

class SamplePageView(TemplateView):
    template_name = "core/sample.html"