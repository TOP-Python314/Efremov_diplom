# Generated by Django 5.0.7 on 2024-09-02 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_usercreateddish_category_alter_usercreateddish_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercreateddish',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='user_dish_image/'),
        ),
    ]
