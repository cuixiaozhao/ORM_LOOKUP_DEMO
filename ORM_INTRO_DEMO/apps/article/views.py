from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Article
from django.utils.timezone import now, localtime


# Create your views here.
def article_view(request):
    # article = Article(removed=False)
    # article.save()
    article = Article(title='abc',create_time=now())
    article.save()
    return HttpResponse("执行成功！")



