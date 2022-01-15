# Generated by Django 3.2 on 2022-01-15 19:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_alter_booking_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]