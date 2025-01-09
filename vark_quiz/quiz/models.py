from django.db import models

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
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
