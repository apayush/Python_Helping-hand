# Generated by Django 4.1.5 on 2023-02-24 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0032_alter_vol_acceptance_delivered_dt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vol_acceptance',
            name='delivered_dt',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='vol_acceptance',
            name='received_dt',
            field=models.DateField(),
        ),
    ]
