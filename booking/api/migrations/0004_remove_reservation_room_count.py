# Generated by Django 3.2.9 on 2021-11-21 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211121_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='room_count',
        ),
    ]
