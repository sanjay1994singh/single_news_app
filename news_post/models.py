from django.db import models
from category.models import Category

from author.models import NewsPostAuthor


# Create your models here.
class NewsPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='news_post_image', null=True, blank=True)
    author = models.ForeignKey(NewsPostAuthor, on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'news_post_master'
