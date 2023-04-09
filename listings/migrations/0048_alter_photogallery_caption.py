# Generated by Django 4.1.4 on 2023-04-08 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0047_rename_address_addressgeo_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photogallery',
            name='caption',
            field=models.CharField(blank=True, choices=[('bedroom', 'Bedroom'), ('indoor', 'Indoor'), ('outdoor', 'Outdoor'), ('kitchen', 'Kitchen'), ('bathroom', 'Bathroom'), ('view', 'View')], max_length=255),
        ),
    ]
