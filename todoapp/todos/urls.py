from django.urls import re_path
from todos.views import TodoActiveListView, TodoCreateView, TodoCompletedListView, TodoToggleCompleteAjaxView

urlpatterns = [
    re_path(r'^active/$', TodoActiveListView.as_view(), name="active_list"),
    re_path(r'^completed/$', TodoCompletedListView.as_view(), name="completed_list"),
    re_path(r'^create/$', TodoCreateView.as_view(), name="create"),
    re_path(r'^done/$', TodoToggleCompleteAjaxView.as_view(), name="done"),
]
