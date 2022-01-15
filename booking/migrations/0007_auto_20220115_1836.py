# Generated by Django 3.2 on 2022-01-15 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20220115_1831'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='primary_Mobile',
            new_name='mobile',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='second_Mobile',
        ),
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]