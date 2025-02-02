from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class WebsiteContact(admin.ModelAdmin):
    list_display = ['name', 'subject', 'created_date', 'updated_date',]
    search_fields = ['name', 'subject', 'message']
    # date_hierarchy = 'created_date'
    list_filter = ['email',]
    ordering = ['updated_date',]
