from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, FormView
from todos.forms import TodoCreateForm
from todos.models import Todo


class TodoActiveListView(LoginRequiredMixin, TemplateView):
    template_name = "todos/active_list.html"
    tab_name = "active"

    def get_context_data(self, **kwargs):
        kwargs["todos"] = Todo.objects.filter(done=False)
        return super(TodoActiveListView, self).get_context_data(**kwargs)


class TodoCompletedListView(LoginRequiredMixin, TemplateView):
    template_name = "todos/completed_list.html"
    tab_name = "completed"

    def get_context_data(self, **kwargs):
        kwargs["todos"] = Todo.objects.filter(done=True)
        return super(TodoCompletedListView, self).get_context_data(**kwargs)


class TodoCreateView(LoginRequiredMixin, FormView):
    form_class = TodoCreateForm
    success_url = reverse_lazy("todos:active_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(TodoCreateView, self).form_valid(form)



