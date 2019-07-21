from django.db import models


class Fish(models.Model):
    fishType = models.CharField(max_length=20)
    farmerId = models.CharField(max_length=20)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.fishType
