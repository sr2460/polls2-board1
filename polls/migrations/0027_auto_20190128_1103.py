# Generated by Django 2.0.2 on 2019-01-28 02:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0026_auto_20190127_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_limit',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 4, 2, 3, 5, 725576, tzinfo=utc), verbose_name='公開期限'),
        ),
    ]
