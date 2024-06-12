from django.contrib import admin
from .models import Banner, BannerImage


# Register your models here.
class BannerAdmin(admin.ModelAdmin):
    list_display = ('banner_code', 'banner_title', 'id')


class BannerImageAdmin(admin.ModelAdmin):
    list_display = ('banner_id', 'banner_code', 'img', 'id')

    def banner_code(self, obj):
        return obj.banner.banner_code


admin.site.register(Banner, BannerAdmin)
admin.site.register(BannerImage, BannerImageAdmin)
