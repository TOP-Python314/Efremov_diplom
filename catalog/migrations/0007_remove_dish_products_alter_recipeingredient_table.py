# Generated by Django 5.0.7 on 2024-08-18 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_recipeingredient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='products',
        ),
        migrations.AlterModelTable(
            name='recipeingredient',
            table='dishes_products',
        ),
    ]
