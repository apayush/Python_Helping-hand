# Generated by Django 4.1.5 on 2023-02-22 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0018_alter_donation_area_alter_donation_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='area',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='city',
        ),
    ]
