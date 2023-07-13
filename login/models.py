from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Organisation(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    organisation_name=models.CharField(max_length=100)
    organisation_domain=models.CharField(max_length=50)