# Generated by Django 3.1.4 on 2020-12-22 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='name',
            new_name='location_name',
        ),
    ]
