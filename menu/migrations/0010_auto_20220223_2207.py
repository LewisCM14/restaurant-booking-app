# Generated by Django 3.2 on 2022-02-23 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_starter_display'),
    ]

    operations = [
        migrations.AddField(
            model_name='dessert',
            name='display',
            field=models.IntegerField(choices=[(0, 'Off'), (1, 'On')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drink',
            name='display',
            field=models.IntegerField(choices=[(0, 'Off'), (1, 'On')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='main',
            name='display',
            field=models.IntegerField(choices=[(0, 'Off'), (1, 'On')], default=1),
            preserve_default=False,
        ),
    ]
