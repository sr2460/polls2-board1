# Generated by Django 2.0.2 on 2019-01-12 02:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20181230_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_limit',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 19, 2, 24, 32, 77893, tzinfo=utc), verbose_name='公開期限'),
        ),
    ]
