from django.db import models

class FeedbackData(models.Model):
    name = models.CharField(max_length=30)
    datetime = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField(max_length=100)
