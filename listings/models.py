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

    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Listings, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    



