# Generated by Django 5.0.7 on 2024-08-27 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_userprofile_profile_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profile_image_url',
            new_name='profile_image',
        ),
    ]
