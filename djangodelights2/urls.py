"""djangodelights2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from inventory import views
# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('ingredient_list/', views.IngredientsView.as_view(), name='ingredients'),
    path('ingredient_list/create', views.AddIngredientsView.as_view(), name='add_ingredient'), 
    path('menu_list/', views.MenuListView.as_view(), name='menu_list'),  
    path("menu_list/create", views.AddMenuView.as_view(), name="add_menu"),
    path("purchases/", views.PurchaseView.as_view(), name="purchases_list"),
    path("purchases/create", views.AddPurchaseView.as_view(), name="add_purchase"),
    path("profit_revenue", views.ProfitView, name="profit_revenue"),
    path("recipe_requirements", views.RecipeRequirementsListView.as_view(), name="recipe_requirements"),


]
