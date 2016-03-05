from django.contrib import admin
from todos.models import ToDo


class ToDoAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "done", "date_created")
    list_filter = ("done", "date_created")

admin.site.register(ToDo, ToDoAdmin)
