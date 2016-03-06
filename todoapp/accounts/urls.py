from accounts.views import UserRegistrationView
from django.conf.urls import url

urlpatterns = [
    url(r'^register/$', UserRegistrationView.as_view(), name="register"),
    url(r'^login/$', "django.contrib.auth.views.login", {"template_name": "accounts/login.html"}, name="login"),
    url(r'^logout/$', "django.contrib.auth.views.logout", {"next_page": "/"}, name="logout"),
]
