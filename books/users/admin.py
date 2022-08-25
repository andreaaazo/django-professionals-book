from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

CURRENT_USER = get_user_model()

# Register your models here.
class CustomAdmin(UserAdmin):
    model = CURRENT_USER
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ["username", "email", "password"]


admin.site.register(CURRENT_USER, CustomAdmin)
