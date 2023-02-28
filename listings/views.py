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
    
    listings = Listings.objects.filter(listing_type=listing_type)
    listing_type = listing_type
    listing_count = len(listings)
    print(listing_count)
    context={"cottages":listings,"listing_type":listing_type}
    return render(request,'listings/stay.html',context)

def Search(request):
    listingType = request.GET.get('listing-type')
    locationType = request.GET.get('location-type')
    adults = request.GET.get('adults')
    children = request.GET.get('children')
    total_guests = int(adults) + int(children)
    minPrice = request.GET.get('price-range-min')
    maxPrice = request.GET.get('price-range-max')
    listings = Listings.objects.filter(listing_type=listingType)
    print(listings)
    context= {
        "listing_type":listingType,
        "location_type":locationType,
        "guests":total_guests,        
        "max_price":maxPrice,
        "listings":listings,
        "is_searched":True
    }
    return render(request,'listings/search.html', context)
