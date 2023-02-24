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
