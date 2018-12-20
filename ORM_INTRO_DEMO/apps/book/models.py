from django.db import models


# Create your models here.
class Book(models.Model):
    """书籍"""
    id = models.AutoField(primary_key=True)  # 代表是一个主键；
    name = models.CharField(max_length=100, null=False, verbose_name='书籍名称')
    author = models.CharField(max_length=100, null=False, verbose_name='书籍作者')
    price = models.FloatField(null=False, default=0, verbose_name="书籍价格")

    def __str__(self):
        # 按照如下格式进行打印：
        return "<Book:({name},{author},{price})>".format(name=self.name, author=self.author, price=self.price)


class Publisher(models.Model):
    """出版社"""
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=True)
