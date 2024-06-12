from django.contrib import admin
from .models import Advertisement


# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('adv_code', 'adv_title', 'id')


admin.site.register(Advertisement, AdvertisementAdmin)
