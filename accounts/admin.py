from django.contrib import admin

# Register your models here.
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'city', 'country', 'middle_name')  # Поля, отображаемые в списке
    search_fields = ('user__username', 'city', 'country')  # Поля для поиска
    list_filter = ('city', 'country')  # Фильтры по городу и стране
    ordering = ('user',)  # Порядок сортировки
    fieldsets = (
        (None, {
            'fields': ('user', 'profile_image', 'bio', 'age', 'city', 'country', 'middle_name')
        }),
    )
    readonly_fields = ('profile_image_url',)  # Установка поля для просмотра изображения как только для чтения
