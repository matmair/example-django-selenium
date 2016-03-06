from django.conf.urls import url
from todos.views import TodoIndexView


urlpatterns = [
    url(r'^$', TodoIndexView.as_view(), name="index"),
]
