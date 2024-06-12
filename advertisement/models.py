from django.db import models


# Create your models here.
class Advertisement(models.Model):
    adv_code = models.CharField(max_length=100, null=True)
    adv_title = models.CharField(max_length=100, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'advertisement'


class AdvertisementImage(models.Model):
    adv = models.ForeignKey(Advertisement, on_delete=models.CASCADE, null=True)
    img = models.ImageField(upload_to='banner_image', null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'advertisement_image'
