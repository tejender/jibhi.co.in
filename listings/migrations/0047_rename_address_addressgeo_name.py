# Generated by Django 4.1.4 on 2023-04-07 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0046_addressgeo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addressgeo',
            old_name='address',
            new_name='name',
        ),
    ]
