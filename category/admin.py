from django.contrib import admin
from .models import Category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'created_date']


admin.site.register(Category, CategoryAdmin)
