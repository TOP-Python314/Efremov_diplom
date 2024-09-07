from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from . import models
from . import forms

""" Главная страница """    
def main(request):
    return render(request, 'index.html')
    
""" Страница продуктов """    
def products(request):
    products_list = models.Product.objects.all()
    return render(request, 'products.html', {'products': products_list})

""" Страница блюд """    
def dishes(request):
    dishes_list = models.Dish.objects.prefetch_related('ingredients__product').all()
    
    for dish in dishes_list:
        dish.ingredients_list = ', '.join([f"{ingredient.product.name}: {ingredient.weight} гр." for ingredient in dish.ingredients.all()])
    
    return render(request, 'dishes.html', {
        'dishes': dishes_list
    })
    
@login_required
def add_user_dish(request):
    if request.method == 'POST':
        dish_id = request.POST.get('dish_id')  # Получаем ID блюда
        dish = models.Dish.objects.get(id=dish_id)  # Получаем объект блюда
        if dish_id is None:
            return redirect(reverse('dishes'))

        try:
            dish = models.Dish.objects.get(id=int(dish_id))
            # Проверка, существует ли запись для текущего пользователя и блюда
            if not models.UserDish.objects.filter(user=request.user, dish=dish).exists():
                models.UserDish.objects.create(user=request.user, dish=dish)
                messages.success(request, 'Рецепт успешно добавлен!')  # Сообщение об успешном добавлении
            else:
                messages.warning(request, 'Этот рецепт уже добавлен!')  # Сообщение о том, что рецепт уже существует

        except models.Dish.DoesNotExist:
            return redirect(reverse('dishes'))

        # Перенаправляем на ту же страницу с блюдами
        return HttpResponseRedirect(reverse('dishes'))

    return HttpResponseRedirect(reverse('dishes')) 
    
""" Добавление продукта """
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list') 
    else:
        form = ProductForm()
    
    return render(request, 'add_product.html', {'form': form})


""" Страница сохраненных блюд """    
@login_required
def saved_dishes(request):
    user_dishes = models.UserDish.objects.filter(user=request.user)  
    added_dishes = [user_dish.dish for user_dish in user_dishes]
    created_dishes = models.UserCreatedDish.objects.filter(user=request.user)  # Получаем созданные блюда для текущего пользователя
    # Объединяем блюда и помечаем их тип
    for dish in added_dishes:
        dish.ingredients_list = ', '.join([
            f"{ingredient.product.name}: {ingredient.weight} гр." 
            for ingredient in dish.ingredients.all()
        ])
    
    for created_dish in created_dishes:
        created_dish.ingredients_list = ', '.join([
            f"{user_created_dish_product.product.name}: {user_created_dish_product.weight} гр." 
            for user_created_dish_product in models.UserCreatedDishProduct.objects.filter(dish=created_dish)
        ])

    dishes = list(added_dishes) + list(created_dishes)
    for dish in dishes:
        dish.type = 'created' if isinstance(dish, models.UserCreatedDish) else 'added'

    return render(request, 'saved_dishes.html', {
        'dishes': dishes,
    })

def user_create_dish(request):
    products = models.Product.objects.all()
    categories = models.Dish.objects.exclude(categorys='').values_list('categorys', flat=True).distinct()
    
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        images = request.FILES.get('images')
        category = request.POST.get('category')
        recipes = request.POST.get('recipes')

        if all([name, recipes]):
            existing_dish = models.UserCreatedDish.objects.filter(name=name, user=request.user).first()
            if existing_dish:
                error_message = "Такое блюдо уже создано."
                return render(request, 'user_create_dish.html', {
                    'error': error_message,
                    'products': products,
                    'categories': categories,
                })

            # Создаем новое блюдо и сохраняем его в базе данных
            new_dish = models.UserCreatedDish(
                user=request.user,  # Привязываем к текущему пользователю
                name=name,
                images=images,
                category=category,
                recipes=recipes,
            )

            try:
                new_dish.save()
                # Получаем ингредиенты
                product_ids = request.POST.getlist('products')
                weights = request.POST.getlist('weights')
                # Создание взаимосвязей
                for product_id, weight in zip(product_ids, weights):
                    if weight and weight.isdigit():  # Проверка, что вес введен и является числом
                        user_created_dish_product = models.UserCreatedDishProduct(
                            dish=new_dish,
                            product_id=product_id,
                            weight=float(weight)  # Преобразование веса в float
                        )
                        user_created_dish_product.save()

                return redirect('saved_dishes')

            except Exception as e:
                print("Ошибка при сохранении блюда:", e)
                return render(request, 'user_create_dish.html', {
                    'error': "Произошла ошибка при сохранении.",
                    'products': products,
                    'categories': categories,
                })
        
        return render(request, 'user_create_dish.html', {
            'error': "Заполните все обязательные поля.",
            'products': products,
            'categories': categories,
        })

    return render(request, 'user_create_dish.html', {
        'products': products,
        'categories': categories,
    })
""" Удаление блюда """
@csrf_exempt
def delete_user_dish(request, dish_id):
    if request.method == 'POST':  # Используем POST для удаления
        try:
            user_dish = models.UserDish.objects.get(dish_id=dish_id, user=request.user)
            user_dish.delete()
            messages.success(request, 'Блюдо успешно удалено.')
            return redirect('profile') 
        except models.UserDish.DoesNotExist:
            messages.error(request, 'Блюдо не найдено.')
            return redirect('profile')
        except Exception as e:
            print(f"Ошибка при удалении блюда: {e}")
            messages.error(request, 'Произошла ошибка на сервере.')
            return redirect('saved_dishes')

    return redirect('saved_dishes')


def delete_user_created_dish(request, dish_id):
    if request.method == 'POST':
        dish = get_object_or_404(models.UserCreatedDish, id=dish_id)

        if dish.user == request.user:
            dish.delete()
            messages.success(request, 'Блюдо успешно удалено.')
        else:
            messages.error(request, 'Вы не имеете права удалять это блюдо.')

        return redirect('saved_dishes')  

    return redirect('saved_dishes')



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
                images=images,  
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
                
                return redirect('saved_dishes')
                 
            except Exception as e:
                print("Ошибка при сохранении блюда:", e)
                return render(request, 'created_dishes.html', {
                    'error': "Произошла ошибка при сохранении."
                })
        # Перенаправление на страницу со всеми блюдами
        return redirect('saved_dishes')
    return redirect('created_dishes_view')
      
def created_dishes_view(request):
    products_list = models.Product.objects.all().order_by('name')
    created_dishes = models.Dish.objects.all()
    return render(request, 'created_dishes.html', {
        'products': products_list,
        'created_dishes': created_dishes,
    })
