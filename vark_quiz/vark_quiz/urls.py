from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include('quiz.urls')),
    path('accounts/', include('allauth.urls')),
    path('', views.home, name='home')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)