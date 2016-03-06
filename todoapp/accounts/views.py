from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import UserRegistrationForm
from django.views.generic import FormView


class UserLoginView(FormView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    success_url = "/"


class UserRegistrationView(FormView):
    template_name = "accounts/register.html"
    form_class = UserRegistrationForm
    success_url = "/"
