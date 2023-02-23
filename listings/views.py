from django.shortcuts import render
from .models import Host

# Create your views here.

def Home(request):
    hosts = Host.objects.all()
    
    active_page='home';

    context={'active_page':active_page,"hosts":hosts}
    return render(request, 'listings/home.html',context)

def Test(request):
    active_page='home';
    context={'active_page':active_page}
    return render(request, 'listings/test.html',context)
