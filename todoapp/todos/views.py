from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, FormView
from todos.forms import TodoCreateForm


class TodoActiveListView(TemplateView):
    template_name = "todos/active_list.html"


class TodoCompletedListView(TemplateView):
    template_name = "todos/completed_list.html"


class TodoCreateView(FormView):
    form_class = TodoCreateForm
    success_url = reverse_lazy("todos:active_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(TodoCreateView, self).form_valid(form)



