#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 项目名称:ORM_INTRO_DEMO
# 文件名称:urls.py
# 用户名:TQTL
# 创建时间:2018/11/30 15:02
from django.urls import path
from article import views

urlpatterns = [
    path('index', views.article_view, name='index')
]
