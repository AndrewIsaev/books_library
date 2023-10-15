from django.contrib.auth.forms import UserCreationForm

from core.models import User


class RegisterForm(UserCreationForm):
    """
    A custom form for user registration.

    This form is used for user registration within the application. It extends
    the built-in 'UserCreationForm' and includes fields for username, password, and
    password confirmation.

    Attributes:
        None.

    Methods:
        None.
    """

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
