from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template
from django.template.response import TemplateResponse

# Create your views here.

from . import models
from . import forms

""" Главная страница """    
def main(request):
    return render(request, 'index.html')
    
""" Страница продуктов """    
def products(request):
    products_list = models.Product.objects.using('food_items').all()
    return render(request, 'products.html', {'products': products_list})

""" Страница продуктов """    
def dishes(request):
    dishes_list = models.Dish.objects.using('food_items').all()
    
    return render(request, 'dishes.html', {
        'dishes': dishes_list
    })

""" Добавление продукта """
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Замените на имя вашего URL для списка продуктов или другую страницу
    else:
        form = ProductForm()
    
    return render(request, 'add_product.html', {'form': form})

""" Страница калькулятора """       
def calculator(request):
    products_list = models.Product.objects.using('food_items').all()
    return render(request, 'calculator.html', {'products': products_list})

# """ Страница профиля """        
# def profile(request):
    # return render(request, 'profile.html')

""" Страница сохраненных блюд """    
def saved_dishes(request):
    
    added_dishes = models.Dish.objects.using('food_items').all()  # Получаем все блюда из базы данных
    created_dishes = models.Dish.objects.using('food_items').all()  # Получаем созданные блюда
    
    return render(request, 'saved_dishes.html', {
        'added_dishes': added_dishes,
        'created_dishes': created_dishes,
    })


""" Страница создания рецепта """        
def created_dishes(request): 
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
        
        if all([name, proteins, fats, carbs, kcals, areas, categorys, recipes]):
            existing_dish = models.Dish.objects.filter(name=name).first()
            if existing_dish:
                # Если блюдо существует, возвращаем сообщение об ошибке
                error_message = "Такое блюдо уже создано."
                return render(request, 'created_dishes.html', {
                    'error': error_message,
                })    
            # Создаем новое блюдо и сохраняем его в базе данных
            new_dish = models.Dish(
                name=name,
                images=images if images else None,  
                proteins=proteins,
                fats=fats,
                carbs=carbs,
                kcals=kcals,
                areas=areas,
                categorys=categorys,
                recipes=recipes
            )
            
            try:
                new_dish.save(using='food_items')
                # Получаем ингридиенты
                ingredient_forms = []
                products = request.POST.getlist('products')
                weights = request.POST.getlist('weights')
                for product_id, weight in zip(products, weights):
                    if weight: 
                        ingredient_forms.append((product_id, weight))        
                
                 # сохраняем игридиенты           
                for product_id, weight in ingredient_forms:
                    
                    models.RecipeIngredient.objects.create(dish_id=new_dish.id, product_id=product_id, weight=weight)
                
                    
                return render(request, 'created_dishes.html',{
                    'products': products_list,
                    'created_dishes': created_dishes,
                })
                 
            except Exception as e:
                print("Ошибка при сохранении блюда:", e)
                # import traceback
                # traceback.print_exc()
                return render(request, 'created_dishes.html', {
                    'error': "Произошла ошибка при сохранении."
                })

        # Перенаправление на страницу со всеми блюдами
        return redirect('saved_dishes')

    # Получаем созданные блюда
    created_dishes = models.Dish.objects  
    
    return redirect('created_dishes')
      
def created_dishes_view(request):
    products_list = models.Product.objects.using('food_items').all().order_by('name')
    return render(request, 'created_dishes.html', {
        'products': products_list,
        'created_dishes': created_dishes,
    })
    
def added_dishes():
    ...