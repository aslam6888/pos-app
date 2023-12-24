from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    quantity = models.IntegerField(null=True, blank=True)
    track_inventory = models.BooleanField(null=True, blank=True, default=False)
    image = models.ImageField(upload_to='media/products', null=True, blank=True)

    def __str__(self):
        return self.name