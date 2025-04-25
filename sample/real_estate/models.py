from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#creating models for Apartment

class Apartment(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(unique=True, max_length=100, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    posted_date = models.DateTimeField(auto_now=True)
    place = models.CharField(max_length=100, blank=False, null=False)
    bedroom_count = models.PositiveIntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.id}-{self.name}-{self.address}"
