# Generated by Django 4.1.4 on 2023-03-26 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0029_listings_banner_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='place_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]