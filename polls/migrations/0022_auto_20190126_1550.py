# Generated by Django 2.0.2 on 2019-01-26 06:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_auto_20190126_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_limit',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 2, 6, 50, 43, 460024, tzinfo=utc), verbose_name='公開期限'),
        ),
    ]
