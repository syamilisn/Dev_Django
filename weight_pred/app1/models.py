from datetime import date
from django.db import models

class Measure(models.Model):
    weight = models.FloatField()
    waist = models.FloatField()
    hip = models.FloatField()
    bust  = models.FloatField()
    arms  = models.FloatField()
    thigh = models.FloatField()
    bottom = models.FloatField()
    date = models.DateField()
    def __str__(self):
        return self.date,self.weight, 