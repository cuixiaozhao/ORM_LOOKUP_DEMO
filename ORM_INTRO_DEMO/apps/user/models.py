from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=20)


class UserExtension(models.Model):
    birthday = models.DateTimeField(null=True)
    school = models.CharField(max_length=50, blank=True)
    user = models.OneToOneField('User', on_delete=models.CASCADE,related_name='extention')
