# Generated by Django 5.0.7 on 2024-08-13 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_dish_areas_dish_categorys_dish_image_dish_recipes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='image',
            new_name='images',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='images',
        ),
    ]
