# Generated by Django 4.1.4 on 2023-03-09 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_thumbimages_listings_thumb_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thumbimages',
            old_name='urlq',
            new_name='url1',
        ),
    ]
