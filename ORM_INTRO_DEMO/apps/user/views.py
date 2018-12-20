from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *


# Create your views here.
def one_to_one_view(request):
    user = User.objects.first()
    extension = UserExtension(school="天晴天朗")
    # extension.user = user
    extension.save()
    return HttpResponse("一对一操作成功！")
