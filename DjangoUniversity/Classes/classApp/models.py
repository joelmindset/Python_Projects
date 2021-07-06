from django.db import models


# Create your models here.
class djangoClasse(models.Model):
    title = models.CharField(max_length=60)
    courseNumber = models.IntegerField()
    instructorName = models.CharField(max_length=60)
    duration = models.FloatField()
