from django.contrib import admin
from .models import User, Categories

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'telegram','phone')
    search_fields = ('name', 'telegram')

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ('category_name',)