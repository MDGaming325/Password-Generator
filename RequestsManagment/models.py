from django.db import models

class RequestModel(models.Model):
    length = models.IntegerField()
    symbols = models.BooleanField()
    numbers = models.BooleanField()
