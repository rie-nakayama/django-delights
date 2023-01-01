from django import forms
from .models import Ingredients, MenuItem, Purchases, RecipeRequirements

class MenuItemCreateForm(forms.ModelForm):
  class Meta:
    model = MenuItem
    fields = ("__all__")

class IngredientCreateForm(forms.ModelForm):
  class Meta:
    model = Ingredients
    fields = ("__all__")

class RecipeRequirementsCreateForm(forms.ModelForm):
  class Meta:
    model = RecipeRequirements
    fields = ("__all__")

class PurchasesCreateForm(forms.ModelForm):
  class Meta:
    model = Purchases
    fields = ("__all__")

class IngredientQuantityCreateForm(forms.ModelForm):
  class Meta:
    model = Ingredients
    fields = ("__all__")