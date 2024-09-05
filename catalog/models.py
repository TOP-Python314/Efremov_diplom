from django.db import models
from django.db.models import SmallAutoField, DecimalField, CharField, ImageField, TextField, ForeignKey, ManyToManyField
from django.contrib.auth.models import User

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

class UserDish(models.Model):
    user = ForeignKey(User, related_name='user_dishes', on_delete=models.CASCADE)
    dish = ForeignKey(Dish, related_name='user_dishes', on_delete=models.CASCADE)  # Укажите правильный путь к модели Dish
    ingredients = ManyToManyField('catalog.RecipeIngredient', blank=True)  # Укажите правильный путь к модели RecipeIngredient

    class Meta:
        db_table = 'user_dishes'

    def __repr__(self):
        return f"{self.user.username}'s dish: {self.dish.name}"

class UserCreatedDish(models.Model):
    user = models.ForeignKey(User, related_name='user_created_dishes', on_delete=models.CASCADE)  # Связь с пользователем
    name = models.CharField(max_length=50)  # Название блюда
    images = models.ImageField(upload_to='user_dish_image/', null=True, blank=True)  # Изображение блюда
    category = models.CharField(max_length=50, null=True)
    recipes = models.TextField(null=True)  # Рецепт блюда
    products = models.ManyToManyField(Product, blank=True)  # Укажите правильный путь к модели Product

    class Meta:
        db_table = 'user_created_dishes'

    def __repr__(self):
        return f"{self.user.username}'s created dish: {self.name}"

class UserCreatedDishProduct(models.Model):
    dish = models.ForeignKey(UserCreatedDish, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.FloatField()  # Дополнительное поле, например, для веса

    class Meta:
        db_table = 'user_created_dish_products'
        unique_together = ('dish', 'product')