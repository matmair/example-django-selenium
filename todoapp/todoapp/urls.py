from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from hello.views import HelloView


urlpatterns = [
    url(r'^$', HelloView.as_view()),
    url(r'^todos/', include("todos.urls", namespace="todos")),
    url(r'^accounts/', include("accounts.urls", namespace="accounts")),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
