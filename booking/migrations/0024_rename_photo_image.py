# Generated by Django 3.2 on 2022-02-08 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0023_rename_photos_photo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photo',
            new_name='Image',
        ),
    ]
