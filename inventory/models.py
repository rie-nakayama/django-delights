from django.db import models

# Create your models here.
class Ingredients(models.Model):
    name = models.CharField(max_length = 20)
    quantity = models.DecimalField(decimal_places = 2, max_digits = 10, default=0.00)
    unit = models.CharField(max_length= 20)
    unitprice = models.DecimalField(decimal_places = 2, max_digits = 10, default=0.00)

class MenuItem(models.Model):
    title = models.CharField(max_length= 40)
    price = models.DecimalField(decimal_places = 2, max_digits = 10, default=0.00)

    def __str__(self):
        return f'<MenuItem: {self.title}>'

class RecipeRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.DecimalField(decimal_places = 2, max_digits = 10, default=0.00)


class Purchases(models.Model):
    id = models.IntegerField(primary_key=True )
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField()
