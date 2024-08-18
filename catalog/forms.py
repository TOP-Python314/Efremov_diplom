from django import forms
from .models import Dish, Product, RecipeIngredient

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'recipes']

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['product', 'weight']

