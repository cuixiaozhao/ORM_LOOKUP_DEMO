# Generated by Django 2.1.3 on 2018-11-29 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='removed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
