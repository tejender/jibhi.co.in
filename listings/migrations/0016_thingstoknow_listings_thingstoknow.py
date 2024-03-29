# Generated by Django 4.1.4 on 2023-03-23 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_rename_distance_listings_distance_in_meters'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThingsToKnow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('checkInBefore', models.CharField(max_length=20)),
                ('checkInAfter', models.CharField(max_length=20)),
                ('checkOutBefore', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='listings',
            name='thingsToKnow',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='things_to_know', to='listings.thingstoknow'),
        ),
    ]
