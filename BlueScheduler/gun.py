#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import gevent.monkey
gevent.monkey.patch_all()

import multiprocessing


bind = '127.0.0.1:9288'
#pidfile = 'output/gunicorn.pid'
logfile = 'output/access.log'
errorlog = 'output/error.log'

# 监听队列
backlog = 1024
#启动的进程数
workers = 8
worker_class = "gevent"

x_forwarded_for_header = 'X-FORWARDED-FOR'
