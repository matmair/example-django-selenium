from django.conf.urls import url

urlpatterns = [
    # url(r'^profile/$', "profile", name="profile"),
    url(r'^register/$', "register", name="register"),
    url(r'^login/$', "login", name="login"),
    # url(r'^logout/$', "logout", name="logout"),
]
