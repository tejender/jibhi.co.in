# Generated by Django 4.1.4 on 2023-03-09 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_listings_location_type_listings_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThumbImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_name', models.CharField(max_length=50)),
                ('urlq', models.ImageField(upload_to='images/thumb-images')),
                ('url2', models.ImageField(upload_to='images/thumb-images')),
                ('url3', models.ImageField(upload_to='images/thumb-images')),
                ('url4', models.ImageField(upload_to='images/thumb-images')),
                ('url5', models.ImageField(upload_to='images/thumb-images')),
            ],
        ),
        migrations.AddField(
            model_name='listings',
            name='thumb_images',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.thumbimages'),
        ),
    ]
