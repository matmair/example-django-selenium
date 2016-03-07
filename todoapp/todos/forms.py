from django import forms
from todos.models import Todo


class TodoCreateForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ("text", )
