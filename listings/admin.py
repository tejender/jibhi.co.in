from django.contrib import admin

# Register your models here.
from .models import Host,Amenities,Listings,ThumbImages,PhotoGallery, ThingsToKnow
class ContactAdmin(admin.ModelAdmin):
        list_display = ('id','name', 'email', 'phone', 'address', 'image')



class AmenitiesAdmin(admin.ModelAdmin):
        list_display = ('amenity_name','amenity_icon')


class ListingsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'location', 'capacity', 'num_bedrooms', 'num_bathrooms', 'price_per_night','listing_type','location_type','distance_in_meters',"slug")

class ThumbImagesAdmin(admin.ModelAdmin):
       list_display = ('listing_name',)


class PhotoGalleryAdmin(admin.ModelAdmin):
       list_display = ('caption',)

class ThingsToKnowAdmin(admin.ModelAdmin):
       list_display = ('name','checkInAfter', 'checkInBefore','checkOutBefore')

admin.site.register(Host, ContactAdmin)
admin.site.register(Amenities, AmenitiesAdmin)
admin.site.register(Listings, ListingsAdmin)
admin.site.register(ThumbImages,ThumbImagesAdmin)
admin.site.register(PhotoGallery,PhotoGalleryAdmin)
admin.site.register(ThingsToKnow,ThingsToKnowAdmin)

