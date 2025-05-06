from . import views
from django.urls import path


urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.tweet_list, name='tweet_list'),
    path('tweet_create/', views.tweet_create, name='tweet_create'),
    path('tweet_edit/', views.tweet_edit, name='tweet_edit'),
    path('tweet_edit/<int:tweet_id>/', views.tweet_edit, name='tweet_edit'),
    path('tweet_delete/<int:tweet_id>/', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register'),
    path('tweets/', views.tweet_list, name='tweets'),
    path('search/', views.search_tweet, name='search_tweet'),
     path('profile/', views.user_profile, name='user_profile'),
     path('edit_profile/', views.edit_profile, name='edit_profile'),
]
