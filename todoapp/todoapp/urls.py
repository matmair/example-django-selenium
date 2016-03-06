from django.conf import settings
from django.conf.urls import  include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^', include("todos.urls", namespace="todos")),
    url(r'^accounts/', include("accounts.urls", namespace="users")),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
