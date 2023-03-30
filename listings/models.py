from django.core.validators import FileExtensionValidator

from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Host(models.Model):
    
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='host/dp', blank=True)
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
    

class ThumbImages(models.Model):
   
   listing_name = models.CharField(max_length=50)
   url1 = models.ImageField(upload_to='images/thumb-images')
   url2 = models.ImageField(upload_to='images/thumb-images')
   url3 = models.ImageField(upload_to='images/thumb-images')
   url4 = models.ImageField(upload_to='images/thumb-images')
   url5 = models.ImageField(upload_to='images/thumb-images')  

   def __str__(self):
        return self.listing_name
   

class ThingsToKnow(models.Model):
    name = models.CharField(max_length=255)
    checkInAfter = models.CharField(max_length=20)
    checkInBefore = models.CharField(max_length=20)
    checkOutBefore = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Listings(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
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

    distance_in_meters = models.IntegerField(default=0)
    thumb_images = models.ForeignKey(ThumbImages,on_delete=models.CASCADE,null=True)
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True,default="hi")
    thingsToKnow = models.ForeignKey('ThingsToKnow', on_delete=models.CASCADE, null=True, blank=True)
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Listings, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class PhotoGallery(models.Model):
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name='photos')
    

    image = models.ImageField(upload_to='photo_gallery/', blank=True)
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption

    def save(self, *args, **kwargs):
        # Get the listing's slug and use it to update the image field's upload_to path
        slug = self.listing.slug
        self.image.upload_to = f'photo_gallery/{slug}/'
        super().save(*args, **kwargs)



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


class Testimg(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/testimg/', null=True, blank=True)

    def __str__(self):
        return self.name


    



