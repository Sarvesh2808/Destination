from django.db import models
# Create your models here.


class Destination(models.Model):

    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=260, default='')
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
