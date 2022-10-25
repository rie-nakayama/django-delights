from django.contrib import admin
from .models import Ingredients, MenuItem, Purchases, RecipeRequirements

# Register your models here.
admin.site.register(Ingredients)
admin.site.register(Purchases)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirements)