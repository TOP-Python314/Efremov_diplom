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
    # templ = (settings.BASE_DIR / 'templates/head.html').read_text(encoding='utf-8')   
    # return HttpResponse(templ)
    return render(request, 'index.html')
    
# def products(request):
    # html_dock = TemplateResponse(
        # request,
        # 'products.html',
        # {
            # 'products': models.Product.objects.all(),
        # },
    # )
    # return html_dock
def products(request):
    products_list = models.Product.objects.all()
    return render(request, 'products.html', {'products': products_list})
   
def calculator(request):
    products_list = models.Product.objects.all()
    return render(request, 'calculator.html', {'products': products_list})
    
def profile(request):
    return render(request, 'profile.html')

def dishes(request):
    added_dishes = Dish.objects.filter(type='added')  # Получаем все блюда из базы данных
    created_dishes = Dish.objects.filter(type='created')  # Получаем созданные блюда

    if request.method == 'POST':  # Обработка формы создания нового блюда
        name = request.POST.get('name')
        image = request.POST.get('image')  # Загрузка файла
        proteins = request.POST.get('proteins')
        fats = request.POST.get('fats')
        carbs = request.POST.get('carbs')
        kcals = request.POST.get('kcals')
        areas = request.POST.get('areas')
        categorys = request.POST.get('categorys')
        recipes = request.POST.get('recipes')

        # Создаем новое блюдо и сохраняем его в базе данных
        new_dish = Dish(
            name=name,
            image=image,
            proteins=proteins,
            fats=fats,
            carbs=carbs,
            kcals=kcals,
            areas=areas,
            categorys=categorys,
            recipes=recipes
        )
        new_dish.save()

        # Перенаправление на ту же страницу
        return HttpResponseRedirect(reverse('saved_dishes'))

    # Возвращаем рендеринг, если метод не POST
    return render(request, 'saved_dishes.html', {
        'added_dishes': added_dishes,
        'created_dishes': created_dishes,
    })
def created_dishes():
    ...
    
def added_dishes():
    ...

    
def saved_dishes(request):
    return render(request, 'saved_dishes.html')