# Generated by Django 2.0.2 on 2019-01-24 06:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20190124_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_limit',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 31, 6, 54, 43, 121887, tzinfo=utc), verbose_name='公開期限'),
        ),
    ]
