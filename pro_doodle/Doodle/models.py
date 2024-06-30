from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Sondage(models.Model):
    name = models.CharField(max_length=70)
    lieux = models.CharField(max_length=100)
    date = models.DateField()
    heure = models.TimeField()

class DateSondage(models.Model):
    sondage = models.ForeignKey(Sondage, on_delete=models.CASCADE)
    date = models.DateField()
    votes = models.IntegerField(default=0) 
    class Meta:
        unique_together = ('sondage', 'date')


class Vote(models.Model):
   
    date_sondage = models.ForeignKey(DateSondage, on_delete=models.CASCADE)
 

