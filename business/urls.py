# business 分路由层
from django.urls import path
from . import views

urlpatterns = [
     # 使用URL反向解析方式。
     path('first_page', views.business_first_page, name='url_business_first_page')
]