from django.conf.urls import url
from todos.views import TodoActiveListView, TodoCreateView, TodoCompletedListView

urlpatterns = [
    url(r'^active/$', TodoActiveListView.as_view(), name="active_list"),
    url(r'^completed/$', TodoCompletedListView.as_view(), name="completed_list"),
    url(r'^create/$', TodoCreateView.as_view(), name="create"),
]
