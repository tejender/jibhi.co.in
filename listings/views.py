from django.shortcuts import render
from .models import Listings ,Host

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
    
    active_page='stay'
    listings = Listings.objects.filter(listing_type=listing_type)        
    listing_type = listing_type      
    context={"cottages":listings,"listing_type":listing_type,'active_page':active_page}
    return render(request,'listings/stay.html',context)

def StayAll(request):
    active_page='stay'
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


def Sitemap(request):
    return render(request,'listings/sitemap.html')
