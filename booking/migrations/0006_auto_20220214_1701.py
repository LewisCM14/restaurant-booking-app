# Generated by Django 3.2 on 2022-02-14 17:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_booking_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='phone_number',
        ),
        migrations.AlterField(
            model_name='booking',
            name='mobile',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]