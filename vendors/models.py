from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SeedsProduct(models.Model):
    vendor_name=models.CharField(max_length=100)
    seed_name=models.CharField(max_length=100)
    exweather=models.TextField()
    exph=models.FloatField()
    price=models.FloatField()

    def __str__(self):
        return self.seed_name