#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 项目名称:ORM_LOOKUP_DEMO
# 文件名称:urls.py
# 用户名:TQTL
# 创建时间:2018/12/11 19:55
from django.urls import path
from apps.front import views
urlpatterns = [

    path('',views.index)
]