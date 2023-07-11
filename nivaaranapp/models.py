from django.db import models
import uuid
# Create your models here.
MLModels_Choices=(
    ('violence','violence'),
    ('detection','detection'),
    ('intrusion','intrusion'),
    

)

class MLModels(models.Model):
    type = models.CharField(max_length=30,choices=MLModels_Choices)
    file = models.FileField(upload_to="models/uploads/")

class Label(models.Model):
    name = models.CharField(max_length=50)

class Detection(models.Model):
    labels = models.ForeignKey(Label, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()
    uni_id = models.CharField(max_length=100, default=uuid.uuid4)