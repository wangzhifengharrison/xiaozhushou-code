#!/usr/bin/env python
# -*- encoding=utf-8 -*-


def application(env, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    return [b'Hello World, Hello uWSGI.']
