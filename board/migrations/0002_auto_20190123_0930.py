# Generated by Django 2.0.2 on 2019-01-23 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='namae',
            new_name='name',
        ),
    ]
