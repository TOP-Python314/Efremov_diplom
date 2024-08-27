from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from . import models
from . import forms
# Функция входа
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Проверка пользователя в базе данных db_users
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, 'Неверное имя пользователя или пароль.')
                print("Authentication failed for user:", username)
            else:
                print("Authenticated user:", user.username)  # Здесь можно вывести дополнительную информацию о пользователе
                login(request, user)
                return redirect('main')  # Перенаправляем на главную страницу после входа
        else:
            print(form.errors)
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


# Функция регистрации
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Не сохраняет в БД сразу
            user.set_password(form.cleaned_data['password1'])  # Установка хешированного пароля
            user.save()  # Сохраняем нового пользователя в БД db_users
            username = form.cleaned_data.get('username')
            messages.success(request, f'Учетная запись {username} создана! Теперь вы можете войти.')
            return redirect('login')  # Перенаправляем на страницу логина
        else:
            # Обработка ошибок формы
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        models.UserProfile.objects.create(user=instance)

@login_required
def profile(request):
    try:
        user_profile = models.UserProfile.objects.get(user=request.user)
    except models.UserProfile.DoesNotExist:
        messages.error(request, 'Профиль не найден.')
        return redirect('main')  # Замените на URL по умолчанию

    if request.method == 'POST':
        user_form = forms.UserUpdateForm(request.POST, instance=request.user)  # Обновляем пользователя
        profile_form = forms.UserProfileForm(request.POST, request.FILES, instance=user_profile)  # Обновляем профиль
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()       # Сохраняем данные пользователя
            profile_form.save()    # Сохраняем данные профиля
            return redirect('profile')  # Перенаправление на страницу профиля
            
    else:
        user_form = forms.UserUpdateForm(instance=request.user)
        profile_form = forms.UserProfileForm(instance=user_profile)

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form, 'user': user_profile})
