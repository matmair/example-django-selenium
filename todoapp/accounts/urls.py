from accounts.views import UserRegistrationView
from django.urls import re_path
from django.contrib.auth import views

urlpatterns = [
    re_path(r'^register/$', UserRegistrationView.as_view(), name="register"),
    re_path(r'^login/$', views.LoginView.as_view(), {"template_name": "accounts/login.html"}, name="login"),
    re_path(r'^logout/$', views.LogoutView.as_view(), {"next_page": "/"}, name="logout"),
]
