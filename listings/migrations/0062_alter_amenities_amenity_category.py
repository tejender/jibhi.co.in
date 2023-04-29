# Generated by Django 4.1.4 on 2023-04-28 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0061_amenities_amenity_priority_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenities',
            name='amenity_category',
            field=models.CharField(choices=[('Bathroom', 'Bathroom'), ('Outooor', 'Outdoor'), ('Bedroom and laundry', 'Bedroom and Laundry'), ('Heating and cooling', 'Heating and Cooling'), ('Internet and office', 'Internet and Office'), ('Kitchen and dining', 'Kitchen and Dining'), ('Parking and facilities', 'Parking and Facilities'), ('Home safety', 'Home Safety'), ('Location features', 'Location Features'), ('Services', 'Services'), ('Other', 'Other')], default='Other', max_length=40),
        ),
    ]