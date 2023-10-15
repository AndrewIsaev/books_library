from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from core.forms import RegisterForm
from core.models import User


def home(request):
    """
    Render the home page.

    This function-based view renders the home page of the application.
    It typically displays basic information to users or serves as an entry point
    to the site.

    Args:
        request (HttpRequest): The request object for this view.

    Returns:
        HttpResponse: A rendered HTML page (base.html) for the home page.
    """
    return render(request, "../templates/base.html")


class RegisterView(CreateView):
    """
    A view for user registration.

    This class-based view allows users to register within the application. It uses
    the 'RegisterForm' form to collect user data, and upon successful registration,
    it redirects to the login page.

    Attributes:
        model (User): The user model for registration.
        form_class (RegisterForm): The form for entering user registration data.
        template_name (str): The template used for rendering the registration form.
        success_url (str): The URL to redirect to after successful registration.
    """

    model = User
    form_class = RegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")
