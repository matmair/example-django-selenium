from django.views.generic import TemplateView


class TodoActiveListView(TemplateView):
    template_name = "todos/active_list.html"


class TodoCompletedListView(TemplateView):
    template_name = "todos/completed_list.html"

