from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    item_image = models.ImageField(max_length=255, upload_to='images/')
    active = models.CharField(max_length=1, default='Y')

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)




