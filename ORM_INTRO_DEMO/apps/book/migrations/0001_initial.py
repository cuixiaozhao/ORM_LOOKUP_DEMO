# Generated by Django 2.1.3 on 2018-11-30 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='书籍名称')),
                ('author', models.CharField(max_length=100, verbose_name='书籍作者')),
                ('price', models.FloatField(default=0, verbose_name='书籍价格')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]