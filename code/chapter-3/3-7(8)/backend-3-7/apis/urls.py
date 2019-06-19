#!/usr/bin/python                                                                  
# -*-encoding=utf8 -*-                                                             
# @Author         : imooc
# @Email          : imooc@foxmail.com
# @Created at     : 2018/11/26
# @Filename       : urls.py
# @Desc           :

from django.urls import path

from .views import weather, menu, image

urlpatterns = [
    # path('', weather.helloworld)
    path('weather', weather.WeatherView.as_view()),
    path('menu', menu.get_menu),
    path('image', image.ImageView.as_view()),
    path('image/list', image.ImageListView.as_view())
]