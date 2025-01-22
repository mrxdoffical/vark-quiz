from django.db import models
from django.conf import settings
class Question(models.Model):
    text = models.CharField(max_length=255)

class Answer(models.Model):
    LEARNING_PATTERNS = [
        ('V', 'Visual'),
        ('A', 'Auditory'),
        ('R', 'Reading/Writing'),
        ('K', 'Kinesthetic'),
    ]
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    letter = models.CharField(max_length=1, choices=LEARNING_PATTERNS)

class QuizResult(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
