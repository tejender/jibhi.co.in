from django.shortcuts import render
from .models import Listings 
from .models import NearByPlaces,AddressGeo
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import requests
import json
import googlemaps
from urllib.parse import urlencode
import random


# Create your views here.

def Home(request):
    
    places= NearByPlaces.objects.all()

    active_page='home';

    context={'active_page':active_page,'places':places}
    return render(request, 'listings/home.html',context)

def Test(request):
    active_page='home';
    context={'active_page':active_page}
    return render(request, 'listings/test.html',context)

def Stay(request,listing_type):    
    
    active_page='listings'
    view_type='list'
    view_url='specific'
    listings = Listings.objects.filter(listing_type=listing_type)     
                      
    listing_type = listing_type      
    context={"listings":listings,"listing_type":listing_type,
             'active_page':active_page,'view_type':view_type
             ,'view_url':view_url}
    return render(request,'listings/stay.html',context)

def StayAll(request):
    active_page='listings'
    listing_type='all'
    view_type='list'
    view_url= 'all'
    listings = Listings.objects.all()    
    
                
            

    context={"listings":listings,'active_page':active_page,'listing_type':listing_type,
             'view_type':view_type,'view_url':view_url}
    return render(request,'listings/stay.html',context)

def Search(request):
    listingType = request.GET.get('listing-type')
    locationType = request.GET.get('location-type')
    adults = request.GET.get('adults')
    children = request.GET.get('children')
    maxPrice = request.GET.get('price-range')

    if not adults:
        adults=1

    if not children:
        children=0

    total_guests = int(adults) + int(children)  

    if listingType=='any' and locationType == 'any' :
        listings = Listings.objects.filter(price_per_night__lte=maxPrice,capacity__gte=total_guests)

    elif listingType == 'any' and locationType !='any':
        listings = Listings.objects.filter(location=locationType ,price_per_night__lte=maxPrice,capacity__gte=total_guests)

    elif listingType !='any' and locationType == 'any' :
        listings = Listings.objects.filter(listing=listingType ,price_per_night__lte=maxPrice,capacity__gte=total_guests)

    else:
        listings = Listings.objects.filter(location=locationType,
                 listing_type=listingType,price_per_night__lte=maxPrice,capacity__gte=total_guests)

  
    # listings = Listings.objects.filter(listing_type=listingType)
    
    context= {
        "listing_type":listingType,
        "location_type":locationType,
        "guests":total_guests,        
        "max_price":maxPrice,
        "listings":listings,
        "is_searched":True
    }
    return render(request,'listings/search.html', context)



def ListingDetail(request,slug):
      # Retrieve the listing matching the slug
    listing = Listings.objects.get(slug=slug)
    current_url = request.build_absolute_uri()  
    

    photos = listing.photos.all()
     
    not_bottom_nav=True
    not_top_nav=True   
    map_token = settings.MAP_BOX_TOKEN
    standout_amenities= listing.amenities.filter(amenity_priority=1)


# Get a random sample of 6 amenities from the high-priority amenities
    standout_amenities  = random.sample(list(standout_amenities), k=6)
    
    

    
    context = {'listing': listing,'photos':photos,
               "not_bottom_nav":not_bottom_nav,"not_top_nav":not_top_nav,               
               'current_url':current_url,'map_token':map_token,'standout_amenities':standout_amenities,
               }
    return render(request,'listings/listingDetail.html', context)


def Enquiry(request):
    form_status=False
    slug=""
    if request.method == 'POST':
        form_status=True
        checkin_date = request.POST.get('checkin-date')
        checkout_date = request.POST.get('checkout-date')
        adults = request.POST.get('adults')
        children = request.POST.get('children')
        message = request.POST.get('message')
        name= request.POST.get('name')
        contact = request.POST.get('contact')
        slug = request.POST.get('slug')

        

        context={}
        
        # send email
        subject = 'Booking Enquiry from Jibhi.co.in'
        body=f'Dear Sir,\n\nI am interested in booking the following property:\n{slug}\n\n\nMy details are as follows:\nName: {name}\nContact Number: {contact}\nCheckin Date: {checkin_date}\nCheckout Date: {checkout_date}\nAdults: {adults}\nChildren: {children}\n\n\nMessage:\n{message}\n\nThank you for your assistance. I look forward to hearing from you soon.'
        # body = f'Name: {name}\n\nContact Number: {contact}\n\nProperty: {slug}\n\nCheckin Date: {checkin_date}\n\nCheckout Date: {checkout_date}\n\nAdults: {adults}\n\nChildren: {children}\n\nMessage: {message}'
        sender_email = settings.EMAIL_HOST_USER
        recipient_list = ["kumartejender007@hotmail.com"]
        try:
            send_mail(subject, body, sender_email, recipient_list, fail_silently=False)
            status_message="success"
        except:
            status_message="fail"

    context={"form_status":form_status,"slug":slug,"status_message":status_message}
    return render(request,'listings/enquiry.html',context)


def ContactUs(request):
    active_page="contact"
    context={"active_page":active_page}
    return render(request, 'listings/contact_us.html',context)


def Places(request,slug): 

    placeDetails = NearByPlaces.objects.get(slug=slug)  # Replace with your actual API key
    
    # Send API request and get response
   
    # Extract reviews
    
    context={}
    
    return render(request, 'listings/places.html',context)


def ListingsMap(request,listing_type):
    listings = Listings.objects.filter(listing_type=listing_type)       
    listing_type = listing_type 
    view_type='map' 
    view_url='specific' 
    map_token = settings.MAP_BOX_TOKEN

   
    context={'listings':listings,
             'listing_type':listing_type,'view_type':view_type,
             'view_url':view_url,'map_token':map_token}
    return render(request, 'listings/map.html',context)

def ListingsMapAll(request,):
    listings = Listings.objects.all()
    view_type='map'
    view_url='all'
    listing_type='all'
    map_token = settings.MAP_BOX_TOKEN
   

    addresses = AddressGeo.objects.all()
   
    context={'listings':listings,'view_type':view_type,'listing_type':listing_type,
             'view_url':view_url,'addresses':addresses,'map_token':map_token}
    return render(request, 'listings/map.html',context)


def Sitemap(request):
    return render(request,'listings/sitemap.html')



# def error_500(request):
#     return render(request, '500.html')


# def error_404(request, exception):
#     return render(request, '404.html')
