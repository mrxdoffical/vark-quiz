from django.urls import path
from .views import tips_view

urlpatterns = [
    path('', tips_view, name='tips'),
]