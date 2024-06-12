from django.db import models


# Create your models here.
class Banner(models.Model):
    banner_code = models.CharField(max_length=100, null=True)
    banner_title = models.CharField(max_length=100, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'banner'


class BannerImage(models.Model):
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE, null=True)
    img = models.ImageField(upload_to='banner_image', null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'banner_image'
