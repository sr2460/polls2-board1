# Generated by Django 2.0.2 on 2019-01-12 08:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20190112_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_limit',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 19, 8, 6, 29, 738744, tzinfo=utc), verbose_name='公開期限'),
        ),
    ]
