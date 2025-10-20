from django.db import models

# Create your models here.
class Intro(models.Model):
    """print hello world"""
    text = models.CharField(max_length=50)
    def __str__(self):
        return self.text