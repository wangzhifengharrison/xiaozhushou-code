#!/usr/bin/python                                                                  
# -*-encoding=utf8 -*-                                                             
# @Author         : imooc
# @Email          : imooc@foxmail.com
# @Created at     : 2018/11/21
# @Filename       : weather.py
# @Desc           :

import json
from django.http import HttpResponse, JsonResponse
from thirdparty import juhe

def helloworld(request):
    print('request method: ', request.method)
    print('request META: ', request.META)
    print('request COOKIES: ', request.COOKIES)
    if request.method == 'GET':
        print('request querydict: ', request.GET)
    else:
        print('request querydict: ', request.POST)
    return HttpResponse(content='OK', status=304, content_type='application/text')



def weather(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        data = []
        result = juhe.weather(city)
        result['city_info'] = city
        data.append(result)
        return JsonResponse(data=data, safe=False)
    elif request.method == 'POST':
        data = []
        received_body = request.body.decode('utf-8')
        received_body = json.loads(received_body)
        print(received_body)
        cities = received_body.get('cities')
        for city in cities:
            result = juhe.weather(city)
            result['city_info'] = city
            data.append(result)
        return JsonResponse(data=data, safe=False)
