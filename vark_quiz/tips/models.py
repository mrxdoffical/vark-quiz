from django.db import models

class LearningPattern(models.Model):
    PATTERN_CHOICES = [
        ('V', 'Visual'),
        ('A', 'Auditory'),
        ('R', 'Reading/Writing'),
        ('K', 'Kinesthetic'),
    ]
    pattern = models.CharField(max_length=1, choices=PATTERN_CHOICES, unique=True)

    def __str__(self):
        return self.get_pattern_display()

class Tip(models.Model):
    learning_pattern = models.ForeignKey(LearningPattern, on_delete=models.CASCADE)
    advice = models.TextField()
    link = models.URLField()

    def __str__(self):
        return f"Tip for {self.learning_pattern}"