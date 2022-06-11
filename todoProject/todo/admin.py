from django.contrib import admin
from .models import ToDo 

# Register your models here.
@admin.register(ToDo)
class ToDo(admin.ModelAdmin):
    list_display = ['title', 'complete', 'created_at']
    list_filter = ['complete', 'creted_at']
    readonly_fields = ['created_at']
    
