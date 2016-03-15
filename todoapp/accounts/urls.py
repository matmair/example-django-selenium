from accounts.views import UserRegistrationView
from django.conf.urls import url
from django.contrib.auth import views

urlpatterns = [
    url(r'^register/$', UserRegistrationView.as_view(), name="register"),
    url(r'^login/$', views.login, {"template_name": "accounts/login.html"}, name="login"),
    url(r'^logout/$', views.logout, {"next_page": "/"}, name="logout"),
]
