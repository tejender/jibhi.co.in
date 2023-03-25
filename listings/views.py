from django.shortcuts import render
from .models import Listings 
from .models import NearByPlaces
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import requests
import json
import googlemaps

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
    
    active_page='listinggs'
    listings = Listings.objects.filter(listing_type=listing_type)        
    listing_type = listing_type      
    context={"cottages":listings,"listing_type":listing_type,'active_page':active_page}
    return render(request,'listings/stay.html',context)

def StayAll(request):
    active_page='listings'
    listings = Listings.objects.all()         
    context={"cottages":listings,'active_page':active_page}
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
    photos = listing.photos.all()   
    not_bottom_nav=True
    not_top_nav=True
    
    # Render the template with the listing details
    context = {'listing': listing,'photos':photos,
               "not_bottom_nav":not_bottom_nav,"not_top_nav":not_top_nav}
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
    context={}
    return render(request, 'listings/contact_us.html',context)


def Places(request,slug):
    


   
    placeDetails = NearByPlaces.objects.get(slug=slug) 
    
    
    # place_id = "ChIJAdBq8rSvBTkRCDcaaOBjL4U" # Replace with your own place ID


    api_key = "AIzaSyB4X65PsaEiyT-rdv4YO5gOn6_fMxJ-_tc" # Replace with your actual API key
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={placeDetails.place_id}&fields=name,rating,user_ratings_total,formatted_phone_number,reviews&key={api_key}"

    # Send API request and get response
    response = requests.get(url)
    data = response.json()

    # Extract reviews
    rating = data['result']['rating']
    user_rating_total = data['result']['user_ratings_total']
    
    reviews = data['result']['reviews']


    gmaps = googlemaps.Client(api_key)
    place = gmaps.place(placeDetails.place_id)['result']
    photos = []
    for photo in place.get('photos', []):
        photo_reference = photo.get('photo_reference')
        photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={api_key}"
        photos.append(photo_url)
    

    
    context={'rating':rating,'reviews':reviews,
             'user_rating_total':user_rating_total,
             'placeDetails':placeDetails,'photos':photos}
    return render(request, 'listings/places.html',context)


def Sitemap(request):
    return render(request,'listings/sitemap.html')



# def error_500(request):
#     return render(request, '500.html')


# def error_404(request, exception):
#     return render(request, '404.html')
