from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from core.forms import RegisterForm
from core.models import User


def home(request):
    return render(request, '../templates/base.html')


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")
