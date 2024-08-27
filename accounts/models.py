from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class CustomUser(models.Model):
    # username = models.CharField(max_length=150, unique=True)
    # email = models.EmailField(unique=True)
    # password = models.CharField(max_length=128)  # Храните с использованием хеширования
    # first_name = models.CharField(max_length=30, blank=True)
    # last_name = models.CharField(max_length=30, blank=True)
    
    # class Meta:
        # db_table = 'custom_user'  # Указывает имя таблицы в базе данных
        
    # def __str__(self):
        # return self.username
        
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  
    bio = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)  
    
    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        # Если загружено новое изображение, переименуйте его
        if self.profile_image:
            # Получаем расширение файла
            ext = self.profile_image.name.split('.')[-1]
            # Устанавливаем новое имя файла как ID пользователя
            self.profile_image.name = f"{self.user.id}.{ext}"  # id с расширением
        super().save(*args, **kwargs)
        
    @property
    def profile_image_url(self):
        if self.profile_image:
            return self.profile_image.url
        return '/static/images/default/none_png.png'