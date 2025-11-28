from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('posts/<slug:slug>', views.post_detail, name='post_detail'),
    path('category/<slug:slug>', views.posts_by_category, name='posts_by_category'),

    path('explore/', views.explore_view, name='explore'),
    path('bookstore/', views.bookstore_view, name='bookstore'),
    path('guides/', views.guides_view, name='guides'),
    path('results', views.search_results, name='search_results'),

    path('<str:username>/', views.profile_detail, name='profile_detail'),

]
