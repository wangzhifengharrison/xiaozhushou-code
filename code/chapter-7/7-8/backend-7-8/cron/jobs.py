#!/usr/bin/python
# -*- encoding=utf-8 -*-


import os
import datetime
import logging


logger = logging.getLogger('django')

def demo():
    message = 'Job log in crontab, now: ' + str(datetime.datetime.now())
    print(message)
    logger.info(message)

