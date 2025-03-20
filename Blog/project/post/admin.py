from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'published', 'created_at')
    list_display_links = ('title', 'user')
    list_editable = ('published',)
    search_fields = ('title', 'content', 'user__username', 'category__name')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)