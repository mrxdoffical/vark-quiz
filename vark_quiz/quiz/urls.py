# vark_quiz/quiz/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_home, name='quiz_home'),
    path('question/<int:question_id>/', views.quiz_question, name='quiz_question'),
    path('result/<int:question_id>/', views.quiz_result, name='quiz_result'),
]