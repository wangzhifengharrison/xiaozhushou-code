#!/usr/bin/python                                                                  
# -*-encoding=utf8 -*-                                                             
# @Author         : imooc
# @Email          : imooc@foxmail.com
# @Created at     : 2018/11/30
# @Filename       : image.py
# @Desc           :


import os
from django.views import View
from django.http import Http404, HttpResponse, FileResponse, JsonResponse
from backend import settings
from utils.response import ReturnCode, CommonResponseMixin



def image(request):
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
        print(imgfile)
        if os.path.exists(imgfile):
            data = open(imgfile, 'rb').read()
            # return HttpResponse(data, content_type='image/jpg')
            return FileResponse(open(imgfile, 'rb'), content_type='image/jpg')
        else:
            return Http404()
    elif request.method == 'POST':
        pass

class ImageView(View, CommonResponseMixin):
    def get(self, request):
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
        print(imgfile)
        if os.path.exists(imgfile):
            data = open(imgfile, 'rb').read()
            # return HttpResponse(data, content_type='image/jpg')
            return FileResponse(open(imgfile, 'rb'), content_type='image/jpg')
        else:
            response = self.wrap_json_response(code=ReturnCode.RESOURCE_NOT_FOUND)
            return JsonResponse(data=response, safe=False)

    def post(self, request):
        message = 'post method success.'
        response = self.wrap_json_response(code=ReturnCode.SUCCESS, message=message)
        return JsonResponse(data=response, safe=False)

    def delete(self, request):
        message = 'delete method success.'
        response = self.wrap_json_response(code=ReturnCode.SUCCESS, message=message)
        return JsonResponse(data=response, safe=False)