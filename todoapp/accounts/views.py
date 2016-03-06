from accounts.forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView


class UserRegistrationView(FormView):
    template_name = "accounts/register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("todos:active_list")

    def form_valid(self, form):
        form.save()
        auth_user = authenticate(username=form.data.get("username"), password=form.data.get("password1"))
        if auth_user is not None:
            login(self.request, auth_user)
        return super(UserRegistrationView, self).form_valid(form)

