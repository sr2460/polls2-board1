# Generated by Django 2.0.2 on 2019-01-26 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_good_good'),
    ]

    operations = [
        migrations.RenameField(
            model_name='good',
            old_name='good',
            new_name='post',
        ),
        migrations.AlterField(
            model_name='good',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]