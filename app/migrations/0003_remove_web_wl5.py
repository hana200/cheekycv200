# Generated by Django 3.2.8 on 2022-07-25 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220725_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='web',
            name='wl5',
        ),
    ]
