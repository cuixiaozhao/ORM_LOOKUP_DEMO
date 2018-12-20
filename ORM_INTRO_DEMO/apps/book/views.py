from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Book


# Create your views here.

def book_view(request):
    # 1、使用ORM添加一条数据到数据库中；
    book = Book(name='西游记', author='吴承恩', price='66')
    book.save()

    # 2、进行书籍的查询；get和filter方法以及first方法；
    book1 = Book.objects.get(pk=2)  # 不管主键是id还是nid，都可以；
    book2 = Book.objects.filter(name='西游记')  # <QuerySet [<Book: <Book:(西游记,吴承恩,66.0)>>]>
    book2 = Book.objects.filter(name='西游记').first()  # <Book:(西游记,吴承恩,66.0)>
    print(book2)
    print(book1)

    # 3、删除数据-delete方法；
    book3 = Book.objects.get(pk=5)
    book3.delete()

    # 4、修改数据：先查询出来，再重新赋值，最后save至数据库；
    book4 = Book.objects.get(pk=6)
    book4.price = 1993
    book4.save()# 注意不要忘记save方法；
    return HttpResponse('书籍查询成功！')
