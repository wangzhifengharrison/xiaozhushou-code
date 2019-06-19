#!/usr/bin/python                                                                  
# -*-encoding=utf8 -*-                                                             
# @Author         : dongcia
# @Email          : dongcia@foxmail.com
# @Created at     : 2018/11/2
# @Filename       : proxy.py
# @Desc           :

import backend.settings


def proxy():
    if backend.settings.USE_PROXY:
        return {}
    else:
        return {}
