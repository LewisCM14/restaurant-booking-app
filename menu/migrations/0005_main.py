# Generated by Django 3.2 on 2022-02-23 17:48

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_rename_menustarter_starter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
