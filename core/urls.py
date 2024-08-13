from django.urls import path
import catalog.views
urlpatterns = [
    path('', catalog.views.main),
    path('index', catalog.views.main),
    path('products', catalog.views.products),
    path('calculator', catalog.views.calculator),
    path('profile', catalog.views.profile),
    path('saved_dishes/', catalog.views.saved_dishes),
    path('', catalog.views.dishes, name='dishes'),
    path('added_dishes', catalog.views.added_dishes, name='added_dishes'),
    path('created_dishes', catalog.views.created_dishes, name='created_dishes'), 

]
