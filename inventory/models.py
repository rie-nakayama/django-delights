from django.db import models

# Create your models here.
class Ingredients(models.Model):
    name = models.CharField(max_length = 20)
    quantity = models.IntegerField()
    unit = models.CharField(max_length= 20)
    unitprice = models.IntegerField()

class MenuItem(models.Model):
    title = models.CharField(max_length= 40)
    price = models.IntegerField

class RecipeRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Purchases(models.Model):
    id = models.IntegerField(primary_key=True )
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()