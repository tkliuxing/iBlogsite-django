# -*- coding: utf-8 -*-
import multiprocessing

bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gevent"
worker_connections = 3000
keepalive = 1
pidfile = '/tmp/gunicorn.pid'
#errorlog = '/tmp/gunicorn.error.log'
