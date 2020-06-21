# competition 分路由层
from django.urls import path
from . import views

urlpatterns = [
    # 使用URL反向解析方式。
    path('first_page', views.competion_first_page, name='url_competion_first_page')
]