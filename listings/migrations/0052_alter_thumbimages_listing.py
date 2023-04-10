# Generated by Django 4.1.4 on 2023-04-09 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0051_alter_thumbimages_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbimages',
            name='listing',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thumb_image', to='listings.listings'),
        ),
    ]
