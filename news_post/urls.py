from django.urls import path
from . import views

urlpatterns = [
    path('create_news_post/', views.create_news_post, name='create_news_post'),
    path('update_news_post/', views.update_news_post, name='update_news_post'),
    path('list_news_post/', views.list_news_post, name='list_news_post'),
]
