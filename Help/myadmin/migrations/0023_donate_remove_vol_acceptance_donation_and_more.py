# Generated by Django 4.1.5 on 2023-02-22 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myadmin', '0022_donation_donation_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('don_category', models.CharField(max_length=30)),
                ('contact_person', models.CharField(default=None, max_length=30)),
                ('contact_no', models.CharField(default=None, max_length=30)),
                ('address', models.TextField()),
                ('city', models.CharField(default=None, max_length=30)),
                ('donation_date', models.DateField(default=None)),
                ('area_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myadmin.area')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'donate',
            },
        ),
        migrations.RemoveField(
            model_name='vol_acceptance',
            name='donation',
        ),
        migrations.DeleteModel(
            name='Donation',
        ),
        migrations.AddField(
            model_name='vol_acceptance',
            name='donate',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='myadmin.donate'),
        ),
    ]
