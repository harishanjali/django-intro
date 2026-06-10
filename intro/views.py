from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import UserSignupForm

# Create your views here.

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'home/home.html'

class SignupView(CreateView):
    form_class = UserSignupForm
    template_name = 'singup.html'
    success_url = reverse_lazy('login')