# Generated by Django 4.1.4 on 2023-02-24 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity_name', models.CharField(max_length=40)),
                ('amenity_icon', models.ImageField(upload_to='icons/amenities')),
            ],
        ),
    ]
