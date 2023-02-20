
from django.urls import path, include
from . import views
from .views import Register


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about', views.about),
    path('registration', views.reg),
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
