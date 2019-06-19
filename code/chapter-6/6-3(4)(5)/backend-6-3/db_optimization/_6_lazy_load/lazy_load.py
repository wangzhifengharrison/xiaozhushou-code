#!/usr/bin/python                                                                  
# -*-encoding=utf8 -*-                                                             
# @Author         : imooc
# @Email          : imooc@foxmail.com
# @Created at     : 2018/12/26
# @Filename       : lazy_load.py
# @Desc           :




import os
import time
import django
import random
import hashlib

from backend import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from authorization.models import User
from apis.models import App

# 懒加载
def lazy_load():
    for user in User.objects.all():
        print(user.menu.all())

# 预加载
def pre_load():
    for user in User.objects.prefetch_related('menu'):
        print(user.menu.all())
    pass


if __name__ == '__main__':
    pre_load()