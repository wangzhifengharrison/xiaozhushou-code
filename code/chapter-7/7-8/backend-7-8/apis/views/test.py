#!/usr/bin/python
# -*- encoding=utf-8 -*-


from django.http import HttpResponse


def test(request):
    return HttpResponse("Hello World")
