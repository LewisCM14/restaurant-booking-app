# Generated by Django 3.2 on 2022-02-23 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20220223_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menustarter',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='menustarter',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
