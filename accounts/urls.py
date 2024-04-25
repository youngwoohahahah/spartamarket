from django.urls import path
from . import views

# for Media
from django.conf import settings
from django.conf.urls.static import static


app_name = "accounts"
urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('delete/', views.delete, name="delete"),
    path('update/', views.update, name="update"),
    path('password/', views.change_password, name="change_password"),
    path('profile_photo/', views.profile_photo, name='profile_photo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)