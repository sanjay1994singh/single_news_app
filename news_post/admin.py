from django.contrib import admin
from .models import NewsPost


# Register your models here.
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ['categories', 'title', 'author', 'id', 'created_date']


admin.site.register(NewsPost, NewsPostAdmin)
