from django.db import models
from django.db.models import SmallAutoField, DecimalField, CharField, ImageField, TextField, ForeignKey

# Модель Product
class Product(models.Model):
    id = SmallAutoField(primary_key=True)
    name = CharField(max_length=50)
    images = models.CharField(max_length=255, null=True)
    text = TextField(null=True)
    proteins = DecimalField(max_digits=5, decimal_places=2)
    fats = DecimalField(max_digits=5, decimal_places=2)
    carbs = DecimalField(max_digits=5, decimal_places=2)
    kcals = DecimalField(max_digits=5, decimal_places=2)
    categorys = CharField(max_length=50, null=True)
    areas = CharField(max_length=50, null=True)

    class Meta:
        db_table = 'products'

    def __repr__(self):
        return f'{self.id}\n{self.name}\n{self.kcals}\n{self.proteins}\n{self.fats}\n{self.carbs}'

# Модель Dish
class Dish(models.Model):
    name = CharField(max_length=50, unique=True)
    images = ImageField(upload_to='images/dishes/', null=True, blank=True)
    recipes = TextField(null=True)
    proteins = DecimalField(max_digits=5, decimal_places=2)
    fats = DecimalField(max_digits=5, decimal_places=2)
    carbs = DecimalField(max_digits=5, decimal_places=2)
    kcals = DecimalField(max_digits=5, decimal_places=2)
    categorys = CharField(max_length=50, null=True)
    areas = CharField(max_length=50, null=True)

    class Meta:
        db_table = 'dishes'

    def __repr__(self):
        return f'{self.name}\n{self.kcals}\n{self.proteins}\n{self.fats}\n{self.carbs}'
        
# Модель RecipeIngredient
class RecipeIngredient(models.Model):
    dish = ForeignKey(Dish, related_name='ingredients', on_delete=models.CASCADE)
    product = ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.FloatField()  # вес продукта в граммах

    class Meta:
        db_table = 'dishes_products'

    def __repr__(self):
        return f"{self.product.name} - {self.weight}g"
