# Generated by Django 3.2 on 2022-01-26 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0019_alter_booking_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='notes',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]