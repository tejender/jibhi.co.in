# Generated by Django 4.1.4 on 2023-04-13 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0055_alter_host_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listings',
            name='place_id',
        ),
    ]