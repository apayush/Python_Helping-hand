# Generated by Django 4.1.7 on 2023-02-23 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0029_alter_donate_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate',
            name='city',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myadmin.city'),
        ),
    ]
