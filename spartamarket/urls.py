from django.contrib import admin
from django.urls import path, include

#for Media
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path("accounts/", include("accounts.urls")),
    path("products/", include("products.urls")),
    path("users/", include("users.urls")),
]


#for Media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)