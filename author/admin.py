from django.contrib import admin
from .models import NewsPostAuthor


# Register your models here.
class NewsPostAuthorAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_date', 'id']


admin.site.register(NewsPostAuthor, NewsPostAuthorAdmin)
