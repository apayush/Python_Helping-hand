# Generated by Django 4.1.7 on 2023-02-23 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0028_alter_donate_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate',
            name='city',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='myadmin.city'),
        ),
    ]
