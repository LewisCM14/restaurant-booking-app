# Generated by Django 3.2 on 2022-01-20 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0016_booking_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
    ]
