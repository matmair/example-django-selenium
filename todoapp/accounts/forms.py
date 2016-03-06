from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):

    class Meta:
        fields = ("username", "email")
        model = User
