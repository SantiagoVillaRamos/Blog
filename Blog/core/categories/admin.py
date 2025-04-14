from django.contrib import admin
from .models import Categorie

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'slug', 'publised')
    list_filter = ('publised',)
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-publised', 'title')
