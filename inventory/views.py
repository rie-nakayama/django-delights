from inventory.forms import IngredientCreateForm, MenuItemCreateForm, PurchasesCreateForm
from .models import Ingredients, MenuItem, Purchases, RecipeRequirements
from django.views.generic import ListView, TemplateView, DeleteView, CreateView
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


class HomeView(TemplateView):
  template_name = "inventory/home.html"

  def get_context_data(self):
    context = super().get_context_data()
    context["Ingredients"] = Ingredients.objects.all()
    context["MenuItem"] = MenuItem.objects.all()
    context["Purchases"] = Purchases.objects.all()
    context["RecipeRequirements"] = RecipeRequirements.objects.all()
    return context


# Create your views here.
class IngredientsView(ListView):
    model = Ingredients
    template_name = "inventory/ingredient_list.html"
    

class AddIngredientsView(CreateView):
    model = Ingredients
    template_name = "inventory/add_ingredient.html"
    form_class = IngredientCreateForm

class MenuListView(ListView):
    model = MenuItem
    template_name = "inventory/menu_list.html"

class AddMenuView(CreateView):
    model = MenuItem
    template_name = "inventory/add_menu.html"
    form_class = MenuItemCreateForm


class PurchaseView(ListView):
    model = Purchases
    template_name = "inventory/purchase_list.html"

class RecipeRequirementsListView(ListView):
    model = RecipeRequirements
    template_name = "inventory/recipe_list.html"

class AddPurchaseView(CreateView):
    model = Purchases
    template_name = "inventory/add_purchase.html"
    form_class = PurchasesCreateForm

def ProfitView(request):

     template = loader.get_template('inventory/profit_view.html')
     total_cost = 0
     total_revenue = 0
     purchases = Purchases.objects.all()
     for purchase in purchases:
         recipes = RecipeRequirements.objects.filter(menu_item = purchase.menu_item)
         price = purchase.menu_item.price
         total_revenue = total_revenue + price
         for recipe in recipes:
             recipe_cost = recipe.quantity * recipe.ingredient.unitprice
             total_cost = total_cost + recipe_cost
     profit = total_revenue - total_cost
        
          
     template_context = {
       "profit": profit,
       "total_revenue": total_revenue
     }
     return HttpResponse(template.render(template_context))

