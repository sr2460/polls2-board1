# Generated by Django 2.0.2 on 2019-01-26 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_good'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='good',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='board.Post'),
        ),
    ]
