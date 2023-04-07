from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.db import models

# Register your models here.
from .models import (
       Host,Amenities,Listings,ThumbImages,
       PhotoGallery,ThingsToKnow,NearByPlaces,
       OtherInfoPlaces,Testimg,ListingDescription,AddressGeo
       )
class ContactAdmin(admin.ModelAdmin):
        list_display = ('id','name', 'email', 'phone', 'address', 'image')



class AmenitiesAdmin(admin.ModelAdmin):
        list_display = ('amenity_name','amenity_icon')


class ListingsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'location','place_id', 'capacity', 'num_bedrooms', 'num_bathrooms', 'price_per_night','listing_type','location_type','distance_in_meters',"slug",'latitude','longitude')


class ListingDescriptionAdmin(admin.ModelAdmin):
       formfield_overrides = {
              models.TextField: {'widget': CKEditorWidget}
        }
       list_display = ('listing','complete_description')

class ThumbImagesAdmin(admin.ModelAdmin):
       list_display = ('listing_name','url1','url2','url3','url4','url5',)


class PhotoGalleryAdmin(admin.ModelAdmin):
       list_display = ('listing','image','caption',)

class ThingsToKnowAdmin(admin.ModelAdmin):
       list_display = ('name','checkInAfter', 'checkInBefore','checkOutBefore')


class NearByPlacesAdmin(admin.ModelAdmin):
       formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}

    }
       list_display = ('name','place_id','latitude','longitude','slug','thumb_img')


class OtherInfoPlacesAdmin(admin.ModelAdmin):
       list_display = ('name','distance','transport_mode','drop_off_point_public_transport','drop_off_point_private_transport','trail_length_public_transport','trail_length_private_transport')

class testimgAdmin(admin.ModelAdmin):
       list_display = ('name','image')
       

class AddressGeoAdmin(admin.ModelAdmin):
       list_display = ('name','lat','lang',)

admin.site.register(Host, ContactAdmin)
admin.site.register(Amenities, AmenitiesAdmin)
admin.site.register(Listings, ListingsAdmin)
admin.site.register(ListingDescription,ListingDescriptionAdmin)
admin.site.register(ThumbImages,ThumbImagesAdmin)
admin.site.register(PhotoGallery,PhotoGalleryAdmin)
admin.site.register(ThingsToKnow,ThingsToKnowAdmin)
admin.site.register(NearByPlaces,NearByPlacesAdmin)
admin.site.register(OtherInfoPlaces,OtherInfoPlacesAdmin)
admin.site.register(Testimg,testimgAdmin)
admin.site.register(AddressGeo,AddressGeoAdmin)

