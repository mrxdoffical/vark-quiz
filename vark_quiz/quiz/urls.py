# vark_quiz/quiz/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_home, name='quiz_home'),
    path('question/', views.quiz_question, name='quiz_question'),
    path('results/', views.quiz_result, name='results'),
    path('results/save/', views.quiz_result, name='quiz_result'),  # URL for saving results
]