from django.db import models
import uuid
# Create your models here.

class Label(models.Model):
    name = models.CharField(max_length=50)

class Detection(models.Model):
    labels = models.ForeignKey(Label, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()
    uni_id = models.CharField(max_length=100, default=uuid.uuid4)