from django.contrib import admin
from .models import Post, Category

# Register your models here.

@admin.register(Post)
class BlogPost(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '_empty_'
    list_display = ['id', 'title', 'counted_views', 'status', 'published_date',]
    list_filter = ['status', 'published_date']
    ordering = ['-created_date', 'status',]
    search_fields = ['title', 'content']
# admin.site.register(Post, PostAdmin)

admin.site.register(Category)