# Generated by Django 4.1.4 on 2023-04-03 12:00

from django.db import migrations, models
import django.db.models.deletion
import listings.models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0036_alter_photogallery_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listings',
            name='thumb_images',
        ),
        migrations.RemoveField(
            model_name='thumbimages',
            name='listing_name',
        ),
        migrations.AddField(
            model_name='thumbimages',
            name='listing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thubnails', to='listings.listings'),
        ),
        migrations.AlterField(
            model_name='photogallery',
            name='image',
            field=models.ImageField(blank=True, upload_to=listings.models.get_upload_path),
        ),
    ]