from django.shortcuts import render

from catalog.models import Product, Dish
# Create your views here.
""" Страница калькулятора """       
def calculator(request):
    products_list = Product.objects.all()
    dish_list = Dish.objects.all()
    
    return render(request, 'calculator.html', {
        'products': products_list,
        'dishes': dish_list,
    })
