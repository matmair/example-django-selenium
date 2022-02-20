from django.conf import settings
from django.urls import include, re_path
from django.conf.urls.static import static
from django.contrib import admin
from hello.views import HelloView


urlpatterns = [
    re_path(r'^$', HelloView.as_view()),
    re_path(r'^todos/', include("todos.urls")),  # , "todos")),
    re_path(r'^accounts/', include("accounts.urls")),  #, "accounts")),
    re_path(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
