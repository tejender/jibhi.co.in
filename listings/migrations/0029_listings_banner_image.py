# Generated by Django 4.1.4 on 2023-03-26 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0028_alter_listings_price_per_night'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='banner_image',
            field=models.ImageField(blank=True, upload_to='banner_images/'),
        ),
    ]
