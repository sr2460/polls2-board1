# Generated by Django 2.0.2 on 2019-01-27 06:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0023_auto_20190127_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_limit',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 3, 6, 42, 6, 832334, tzinfo=utc), verbose_name='公開期限'),
        ),
    ]