from django import forms
from .models import Dish, Product, RecipeIngredient, UserCreatedDish

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['id', 'name', 'recipes']

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['product', 'weight']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'images', 'text', 'proteins', 'fats', 'carbs', 'kcals', 'categorys', 'areas']

class UserCreatedDishForm(forms.ModelForm):
    class Meta:
        model = UserCreatedDish
        fields = ['name', 'images', 'recipes', 'products']