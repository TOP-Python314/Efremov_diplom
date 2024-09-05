from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect  # Необходим для перенаправления
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import register, login_view, logout_view

import catalog.views
import accounts.views
import calculator.views
# Функция для перенаправления на страницу входа
def redirect_to_login(request):
    return redirect('/login/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', redirect_to_login, name='redirect_to_login'),  # Перенаправление на страницу входа
    path('index', catalog.views.main, name='main'),  
    path('products', catalog.views.products, name='products'),  
    path('dishes', catalog.views.dishes, name='dishes'), 
    path('add_user_dish/', catalog.views.add_user_dish, name='add_user_dish'),
    path('profile', accounts.views.profile, name='profile'), 
    path('saved_dishes', catalog.views.saved_dishes, name='saved_dishes'), 
    path('delete_user_dish/<int:dish_id>/', catalog.views.delete_user_dish, name='delete_user_dish'),
    path('delete_user_created_dish/<int:dish_id>/', catalog.views.delete_user_created_dish, name='delete_user_created_dish'),
    path('user_create_dish', catalog.views.user_create_dish, name='user_create_dish'),
    path('created_dishes', catalog.views.created_dishes, name='created_dishes'),  
    path('created_dishes_view', catalog.views.created_dishes_view, name='created_dishes_view'), 
    path('calculator', calculator.views.calculator, name='calculator'), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

