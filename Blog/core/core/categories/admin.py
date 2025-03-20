from django.contrib import admin
from .models import Category
# Register your models here.

# clase para administrar la tabla de categorias
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_at', 'updated_at')
    list_filter = ('published', 'created_at', 'updated_at')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)