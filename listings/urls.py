from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name='home'),
    path('test/', views.Test, name='test'),
    path('listings/', views.StayAll, name='listings'),
    path('listings/<str:listing_type>/', views.Stay, name='listings'),
    path('search/', views.Search, name='search'),
    path('listing-detail/<str:slug>/', views.ListingDetail, name='listingDetail'),
    path('sitemap/', views.Sitemap, name='sitemap'),
    path('enquiry/', views.Enquiry, name='enquiry'),
    path('contact/', views.ContactUs, name="contact-us")
]


