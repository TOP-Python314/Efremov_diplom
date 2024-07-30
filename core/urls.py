from django.urls import path
import catalog.views
urlpatterns = [
    path('', catalog.views.main),
    path('products', catalog.views.products),
    path('calculator', catalog.views.calculator),
]
