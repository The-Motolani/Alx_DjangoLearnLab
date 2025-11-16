from django.contrib import admin

# Register your models here.
from .models import Book
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, CustomUserCreationForm


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
list_filter = ('author', 'publication_year')
search_fields = ('title', 'author')

admin.site.register(Book)


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ["username", "email", "date_of_birth", "is_staff"]
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

    admin.site.register(CustomUser, CustomUserAdmin)