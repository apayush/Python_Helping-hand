# Generated by Django 4.1.5 on 2023-03-08 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0037_alter_u_events_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='user',
            field=models.CharField(max_length=20),
        ),
    ]
