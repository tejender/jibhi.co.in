# Generated by Django 4.1.4 on 2023-03-14 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0013_alter_photogallery_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listings',
            name='main_image',
        ),
        migrations.AddField(
            model_name='listings',
            name='distance',
            field=models.IntegerField(default=0),
        ),
    ]
