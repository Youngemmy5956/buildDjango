from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()
    # image = models.ImageField(upload_to='menu_images')

    # def __str__(self):
    #     return self.name