from django.contrib import admin

# Register your models here.
from .models import Host,Amenities,Listings
class ContactAdmin(admin.ModelAdmin):
        list_display = ('name', 'email', 'phone', 'address', 'image')


class AmenitiesAdmin(admin.ModelAdmin):
        list_display = ('amenity_name','amenity_icon')


class ListingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'capacity', 'num_bedrooms', 'num_bathrooms', 'price_per_night')



admin.site.register(Host, ContactAdmin)
admin.site.register(Amenities, AmenitiesAdmin)
admin.site.register(Listings, ListingsAdmin)

