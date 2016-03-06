from django.core.urlresolvers import reverse
from django.views.generic import TemplateView


class HelloView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return reverse("todos:active_list")
        return super(HelloView, self).get(request, *args, **kwargs)


