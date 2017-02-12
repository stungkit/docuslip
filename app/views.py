from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class LoginView(TemplateView):
    template_name = "login.html"

class HomeView(TemplateView):
    template_name = "index.html"

class FieldTripsView(TemplateView):
    template_name = "fieldtrips.html"