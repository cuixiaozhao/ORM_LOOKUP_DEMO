from django.db import models


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey('Category',null=True, on_delete=models.CASCADE,related_name='article')

    class Meta:
        db_table = 'article'


class Category(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'category'
