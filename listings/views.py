from django.shortcuts import render
from .models import Listings ,Host
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

def Home(request):
    cottages = Listings.objects.all()
    
    active_page='home';

    context={'active_page':active_page,"cottages":cottages}
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
    # Render the template with the listing details
    context = {'listing': listing,'photos':photos,"not_bottom_nav":not_bottom_nav}
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
        slug = request.POST.get('slug')
        

        context={}
        
        # send email
        # subject = 'Booking Enquiry from Jibhi.co.in'
        # body = f'Checkin Date: {checkin_date}\nCheckout Date: {checkout_date}\nAdults: {adults}\nChildren: {children}\nMessage: {message}'
        # sender_email = settings.EMAIL_HOST_USER
        # recipient_list = ["work.ushna007@gmail.com"]
        # try:
        #     send_mail(subject, body, sender_email, recipient_list, fail_silently=False)
        #     message="success"
        # except:
        #     message="fail"

    context={"form_status":form_status,"slug":slug}
    return render(request,'listings/enquiry.html',context)




def Sitemap(request):
    return render(request,'listings/sitemap.html')
