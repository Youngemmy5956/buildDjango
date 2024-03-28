from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()
    # image = models.ImageField(upload_to='menu_images')

    def __str__(self):
        return self.name + ' : ' + self.cuisine 
    
    
class Drinks(models.Model):
    drink = models.CharField(max_length=200)
    price = models.IntegerField()
    
    class Drinks(models.Model):
          drink_name = models.CharField(max_length=200)
          price = models.IntegerField()
          
          
    class MenuCategory(models.Model):
          category_name = models.CharField(max_length=200)
          
    class Menu(models.Model):
          menu_item = models.CharField(max_length=200)
          price = models.IntegerField(null=False)
          category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None)