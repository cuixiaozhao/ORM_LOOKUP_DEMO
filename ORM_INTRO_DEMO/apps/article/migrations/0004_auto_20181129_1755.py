# Generated by Django 2.1.3 on 2018-11-29 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20181129_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 29, 17, 55, 52, 63708)),
        ),
        migrations.AddField(
            model_name='article',
            name='removed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
