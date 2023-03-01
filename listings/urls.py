from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name='home'),
    path('test/', views.Test, name='test'),
    path('stay/<str:listing_type>/', views.Stay, name='stay'),
    path('search/', views.Search, name='search'),
    path('sitemap/', views.Sitemap, name='sitemap')
]