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
    path('weather', weather.weather),
    path('menu', menu.get_menu),
    # path('image', image.image)
    path('image', image.ImageView.as_view())
]