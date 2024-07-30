from django.db import models
from django.db.models import SmallAutoField, DecimalField, CharField, ManyToManyField

# Create your models here.
class Product(models.Model):
    id = SmallAutoField(primary_key=True)
    name = CharField(max_length=50)
    proteins = DecimalField(max_digits=5, decimal_places=2)
    fats = DecimalField(max_digits=5, decimal_places=2)
    carbs = DecimalField(max_digits=5, decimal_places=2)
    kcals = DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        db_table = 'products'

    def __repr__(self):
        return f'{id}\n{name}\n{kcals}\n{proteins}\n{fats}\n{carbs}'
        


class Dish(models.Model):
 
    name = CharField(max_length=50, unique=True)
    proteins = DecimalField(max_digits=5, decimal_places=2)
    fats = DecimalField(max_digits=5, decimal_places=2)
    carbs = DecimalField(max_digits=5, decimal_places=2)
    kcals = DecimalField(max_digits=5, decimal_places=2)
    
    products = ManyToManyField('Product', db_table='dishes_products')
    
    class Meta:
        db_table = 'dishes'
        
    def __repr__(self):
        return f'{name}\n{kcals}\n{proteins}\n{fats}\n{carbs}'