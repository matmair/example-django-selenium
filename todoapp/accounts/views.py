from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView


class LoginView(FormView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    success_url = ""
