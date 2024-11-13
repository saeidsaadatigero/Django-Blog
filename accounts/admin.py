from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "age",
        "is_staff",
        'about',
        'photo',
        'twitter_username',  # اضافه کردن فیلدهای جدید
        'facebook_username',
        'instagram_username',
    ]

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ('age', 'about', 'photo', 'twitter_username', 'facebook_username', 'instagram_username')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ('age', 'about', 'photo', 'twitter_username', 'facebook_username', 'instagram_username')}),
        )
admin.site.register(CustomUser, CustomUserAdmin)
