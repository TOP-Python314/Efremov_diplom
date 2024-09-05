from django.db import models
from django.contrib.auth.models import User
import os
from django.core.files.storage import default_storage

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/default.jpg', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        # Проверяем, существует ли объект (например, редактирование профиля)
        if self.pk:  
            old_profile = UserProfile.objects.get(pk=self.pk)
            # Проверяем, изменилось ли изображение
            if old_profile.profile_image and old_profile.profile_image != self.profile_image:
                # Удаляем старое изображение из хранилища, если оно существует
                if default_storage.exists(old_profile.profile_image.name):
                    default_storage.delete(old_profile.profile_image.name)

        # Устанавливаем имя файла для нового изображения
        if self.profile_image:
            ext = os.path.splitext(self.profile_image.name)[1]
            self.profile_image.name = f"{self.user.id}{ext}"

        # Сохраняем объект
        super().save(*args, **kwargs)
        
    @property
    def profile_image_url(self):
        """Возвращает URL изображения профиля или путь по умолчанию."""
        if self.profile_image:
            return self.profile_image.url
        return '/static/images/default/none_png.png'
