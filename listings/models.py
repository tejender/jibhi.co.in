from django.core.validators import FileExtensionValidator

from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
import os
import geocoder

from django.conf import settings
# Create your models here.

class Host(models.Model):
    
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/host/dp', blank=True)
    email = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    

    def __str__(self):
        return self.name
    

    


class Amenities(models.Model):

    amenity_name = models.CharField(max_length=40)
    amenity_icon = models.FileField(upload_to='icons/amenities',validators=[FileExtensionValidator(['svg'])])
    def __str__(self):
        return self.amenity_name
    


   




class Listings(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=19, decimal_places=14 ,default=0.0)
    longitude = models.DecimalField(max_digits=30, decimal_places=14,default=0.0)
    place_id = models.CharField(max_length=255,null=True,blank=True)
    capacity = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    amenities = models.ManyToManyField(Amenities)
    price_per_night = models.IntegerField()        
    owner = models.ForeignKey(Host, on_delete=models.CASCADE)
    banner_image = models.ImageField(upload_to='banner_images/', blank=True)
    listing_type = models.CharField(
        max_length=10,default='hi',
        choices=[
            ('cottage', 'Cottage'),
            ('treehouse', 'Treehouse'),
            ('homestay', 'Homestay'),
            ('a-frame', 'A-Frame'),
            ('camp','Camping'),
            ('dome','Domes'),
            ('mudhosue','Mudhouse')
        ],
    )
    location_type = models.CharField(
        max_length=10,default='roadside',
        choices=[
            ('roadside', 'Roadside'),
            ('uphill', 'Uphill'),
            ('downhill', 'Downhill'),
            ('offroad', 'Offroad'),            
        ],
    )

    thumb_description =  models.TextField(max_length=500,blank=True)
    distance_in_meters = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True,default="hi")
    thingsToKnow = models.ForeignKey('ThingsToKnow', on_delete=models.CASCADE, null=True, blank=True)
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Listings, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



class ThumbImages(models.Model):   
   def get_thumb_upload_path(instance, filename):
    return f'images/thumb_images/{instance.listing}/{filename}'

   listing = models.OneToOneField(Listings, on_delete=models.CASCADE, related_name='thumb_images', null=True, blank=True)
   url1 = models.ImageField(upload_to=get_thumb_upload_path,null=True)
   url2 = models.ImageField(upload_to=get_thumb_upload_path,null=True)
   url3 = models.ImageField(upload_to=get_thumb_upload_path,null=True)
   url4 = models.ImageField(upload_to=get_thumb_upload_path,null=True)
   url5 = models.ImageField(upload_to=get_thumb_upload_path,null=True)  

   def __str__(self):
        return self.listing.slug


class PhotoGallery(models.Model):

    def get_upload_path(instance, filename):
        return f'images/photo_gallery/{instance.listing.slug}/{filename}'

    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to=get_upload_path, blank=True)
    photo_category = models.CharField(max_length=255, blank=True,
                               choices=[
            ('bedroom', 'Bedroom'),
            ('indoor', 'Indoor'),
            ('outdoor', 'Outdoor'),            
            ('kitchen', 'Kitchen'),
            ('bathroom', 'Bathroom'),
            ('view','View')
            ])

    def __str__(self):
        return self.listing.slug


class ThingsToKnow(models.Model):
    listing = models.OneToOneField(Listings, on_delete=models.CASCADE, related_name='things_to_know', null=True, blank=True)
    checkInAfter = models.CharField(max_length=20)
    checkInBefore = models.CharField(max_length=20)
    checkOutBefore = models.CharField(max_length=20)

    def __str__(self):
        return self.listing.name

class ListingDescription(models.Model):
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name='description')
    
    complete_description = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.listing.slug
    
class OtherInfoPlaces(models.Model):
    name = models.CharField(max_length=255)
    distance = models.DecimalField(default=0,max_digits=7,decimal_places=1)
    transport_mode = models.CharField(max_length=255)
    drop_off_point_public_transport = models.CharField(max_length=255)
    drop_off_point_private_transport = models.CharField(max_length=255)
    trail_length_public_transport = models.DecimalField(default=0,max_digits=7,decimal_places=1)
    trail_length_private_transport = models.DecimalField(default=0,max_digits=7,decimal_places=1)
    
    def __str__(self):
        return self.name
    
class NearByPlaces(models.Model):
    name = models.CharField(max_length=255)
    place_id = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    thumb_img = models.ImageField(upload_to='images/places/', null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    other_info = models.ForeignKey(OtherInfoPlaces, on_delete=models.CASCADE, null=True, blank=True)
    latitude = models.DecimalField(default=0,max_digits=30,decimal_places=16)
    longitude = models.DecimalField(default=0,max_digits=30,decimal_places=16)

    # hero_video = models.FileField(upload_to='videos/')
    # video_poster = models.ImageField(upload_to='images/')
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(NearByPlaces, self).save(*args, **kwargs)

    def __str__(self):
        return self.name    



def get_upload_path(instance, filename):
    return f'images/testimg/{instance.name}/{filename}'

class Testimg(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_upload_path, null=True, blank=True)

    def __str__(self):
        return self.name



class AddressGeo(models.Model):
    name = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    lang = models.FloatField(blank=True, null=True)

    
    

    def __str__(self):
        return self.name




