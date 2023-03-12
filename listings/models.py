from django.core.validators import FileExtensionValidator

from django.db import models
from django.utils.text import slugify

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


class Listings(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    amenities = models.ManyToManyField(Amenities)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    main_image = models.ImageField(upload_to='images/cottage/main-images')    
    owner = models.ForeignKey(Host, on_delete=models.CASCADE)
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

    thumb_images = models.ForeignKey(ThumbImages,on_delete=models.CASCADE,null=True)
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True,default="hi")
    

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
    



