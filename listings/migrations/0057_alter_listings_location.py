# Generated by Django 4.1.4 on 2023-04-13 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0056_remove_listings_place_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='location',
            field=models.CharField(choices=[('jibhi', 'Jibhi'), ('tandi', 'Tandi'), ('sojha', 'Sojha'), ('sajwar', 'Sajwar'), ('hirab', 'Hirab'), ('seri', 'Seri'), ('mihar', 'Mihar'), ('narhan', 'Narhan'), ('bahu', 'Bahu')], max_length=255),
        ),
    ]
