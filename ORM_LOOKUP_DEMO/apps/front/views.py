from django.shortcuts import render

from django.http import HttpResponse

# from .models import Article,Category
from .models import *

# Create your views here.


# def index(request):
#     # 1、id =1和 id__exact =1 两者等价；
#     # article = Article.objects.filter(id__exact=1)# 两者等价！
#     # article = Article.objects.filter(id=1) # 两者等价！
#
#     # 2、 区分大小写和不区分大小写！涉及到MySQL数据库的排序规则；# 查看ORM翻译成的SQL语句，仅适用于filter语句中，get会报错！
#     article = Article.objects.filter(title__exact='Hello World')
#     # SELECT `article`.`id`, `article`.`title`, `article`.`content` FROM `article` WHERE `article`.`title` = Hello World
#
#     # 3、None语句的查询；
#     # article = Article.objects.filter(title__exact=None)
#     # SELECT `article`.`id`, `article`.`title`, `article`.`content` FROM `article` WHERE `article`.`title` IS NULL
#
#     # 4、忽略大小写的查询，比如exact和iexact；
#     article = Article.objects.filter(title__iexact='HELLO WORLD')
#     # SELECT `article`.`id`, `article`.`title`, `article`.`content` FROM `article` WHERE `article`.`title` LIKE HELLO WORLD
#     print(article)
#     print(article.query)
#     return HttpResponse('查询成功！')


"""
小结：
1、exact翻译成=；
2、iexact翻译成LIKE；
"""


def index1(request):
    article = Article.objects.filter(pk__exact=1)
    print(type(article))
    print(article)
    print(article.query)
    """
    <class 'django.db.models.query.QuerySet'>
    <QuerySet [<Article: Article object (1)>]>
    SELECT `article`.`id`, `article`.`title`, `article`.`content` FROM `article` WHERE `article`.`id` = 1
    """
    return HttpResponse('index1')


def index2(request):
    # result = Article.objects.filter(title__contains='hello world')
    RESULT = Article.objects.filter(title__icontains='HELLO WORLD')
    print(RESULT)
    print(RESULT.query)

    """
    1、使用contains：
    <QuerySet []>
    SELECT `article`.`id`, `article`.`title`, `article`.`content` FROM `article` WHERE `article`.`title` LIKE BINARY %hello world%
    2、使用icontains：
    <QuerySet [<Article: Article object (3)>]>
    SELECT `article`.`id`, `article`.`title`, `article`.`content` FROM `article` WHERE `article`.`title` LIKE %HELLO WORLD%
    """
    return HttpResponse('contains&icontains的区别，比如LIKE和LIKE BINARY')


def index3(request):
    # 查找文章为1,2,3的文章的分类；
    # articles = Article.objects.filter(id__in=[1, 2, 3])
    # for article in articles:
    #     print(article)
    """
    Article object (1)
    Article object (2)
    Article object (3)
    """

    # categories = Category.objects.filter(article__id__in=[1, 2, 3])
    categories = Category.objects.filter(article__id__in=[1, 2, 3])
    for category in categories:
        print(category)
    """
    Category object (1)
    Category object (1)
    Category object (2)
    """
    return HttpResponse('Django ORM查询中的in语句详解！')
"""
1、in可以指定某个字段是否在某个集合中；
2、进行多表查询的时候，使用双下划线进行连接；
"""