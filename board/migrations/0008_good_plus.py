# Generated by Django 2.0.2 on 2019-01-27 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_auto_20190126_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='plus',
            field=models.IntegerField(default=0),
        ),
    ]