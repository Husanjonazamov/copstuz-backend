# Generated by Django 5.1.3 on 2025-05-24 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_remove_cargolocationmodel_map_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargolocationmodel',
            name='phone',
        ),
    ]
