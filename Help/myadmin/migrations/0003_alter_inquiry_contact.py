# Generated by Django 4.1.5 on 2023-02-12 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_inquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='contact',
            field=models.CharField(max_length=10),
        ),
    ]
