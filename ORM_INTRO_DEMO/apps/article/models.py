from django.db import models
from datetime import datetime

# Create your models here.
class Article(models.Model):
    id = models.BigAutoField(primary_key=True)  # 如果设置自定义id，必须添加primary_key = True
    # 如果在定义字段的时候，如果没有指定null =True,那么默认情况下null = False；
    # removed = models.BooleanField(default=False)
    removed = models.BooleanField(default=False)
    title = models.CharField(max_length=200,default=None)
    create_time = models.DateTimeField(default=datetime.now)


class Author(models.Model):
    username = models.CharField(max_length=100)
    class Meta:
        verbose_name = ""
        verbose_name_plural= verbose_name