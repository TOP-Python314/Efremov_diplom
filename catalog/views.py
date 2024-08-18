from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template
from django.template.response import TemplateResponse

# Create your views here.

from . import models
# from . import forms

def main(request):

    return render(request, 'index.html')
    
def products(request):
    products_list = models.Product.objects.all()
    return render(request, 'products.html', {'products': products_list})
   
def calculator(request):
    products_list = models.Product.objects.all()
    return render(request, 'calculator.html', {'products': products_list})
    
def profile(request):
    return render(request, 'profile.html')
    
def saved_dishes(request):
    print('Saved Dishes')
    added_dishes = models.Dish.objects.all()  # Получаем все блюда из базы данных
    created_dishes = models.Dish.objects.all()  # Получаем созданные блюда
    
    return render(request, 'saved_dishes.html', {
        'added_dishes': added_dishes,
        'created_dishes': created_dishes,
    })
    
def created_dishes(request):

    products_list = models.Product.objects.all()
    
    if request.method == 'POST':  
        name = request.POST.get('name')
        images = request.FILES.get('images')  
        proteins = request.POST.get('proteins')
        fats = request.POST.get('fats')
        carbs = request.POST.get('carbs')
        kcals = request.POST.get('kcals')
        areas = request.POST.get('areas')
        categorys = request.POST.get('categorys')
        recipes = request.POST.get('recipes')
        # Проверяем, чтобы все необходимые поля были заполнены (желательно)
        if name and proteins and fats and carbs and kcals and areas and categorys and recipes:
            existing_dish = models.Dish.objects.filter(name=name).first()
            if existing_dish:
                # Если блюдо существует, возвращаем сообщение об ошибке
                error_message = "Такое блюдо уже создано."
                return render(request, 'created_dishes.html', {
                    'error': error_message,
                    'products': products_list,
                })    
            # Создаем новое блюдо и сохраняем его в базе данных
            new_dish = models.Dish(
                name=name,
                images=images if images else None,  # Раскомментируйте, если хотите использовать изображение
                proteins=proteins,
                fats=fats,
                carbs=carbs,
                kcals=kcals,
                areas=areas,
                categorys=categorys,
                recipes=recipes
            )
            try:
                new_dish.save()
            except Exception as e:
                print("Ошибка при сохранении блюда:", e)
            
            new_dish.save()

        # Перенаправление на страницу со всеми блюдами
        return redirect('created_dishes')

    # Получаем созданные блюда
    created_dishes = models.Dish.objects  
    
def added_dishes():
    ...
    
def created_dishes_view(request):
    return render(request, 'created_dishes.html')    
