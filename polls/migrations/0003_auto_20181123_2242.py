# Generated by Django 2.0.2 on 2018-11-23 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20181123_1720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='title',
        ),
    ]
