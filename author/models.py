from django.db import models

from account.models import CustomUser


# Create your models here.
class NewsPostAuthor(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.name)

    class Meta:
        db_table = 'news_post_author'
