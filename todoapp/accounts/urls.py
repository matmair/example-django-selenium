from accounts.views import UserRegistrationView, UserLoginView
from django.conf.urls import url

urlpatterns = [
    url(r'^register/$', UserRegistrationView.as_view(), name="register"),
    url(r'^login/$', UserLoginView.as_view(), name="login"),
    # url(r'^profile/$', "profile", name="profile"),
    # url(r'^logout/$', "logout", name="logout"),
]
