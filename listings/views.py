from django.shortcuts import render

# Create your views here.

def Home(request):
    active_page='home';
    context={'active_page':active_page}
    return render(request, 'listings/home.html',context)
