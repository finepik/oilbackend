from django.db import models
from django.contrib.auth.models import User
class QA(models.Model):
    question = models.CharField(max_length=225)
    answer = models.CharField(max_length=1000)

    def __str__(self):
        return self.question