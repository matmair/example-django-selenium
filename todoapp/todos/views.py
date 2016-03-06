from django.shortcuts import render
from django.views.generic import TemplateView


class TodoIndexView(TemplateView):
    template_name = "todos/index.html"
