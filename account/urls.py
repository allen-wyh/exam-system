# account 分路由层
from django.urls import path
from . import views

urlpatterns = [
    # 使用URL反向解析方式。
    path('first_page', views.account_first_page, name='url_account_first_page')
]