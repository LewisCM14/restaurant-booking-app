# Generated by Django 3.2 on 2022-02-11 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0030_remove_booking_arrival'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='arrival',
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
    ]
