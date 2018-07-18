#!/usr/bin/env python
# coding: utf-8
# Date  : 2018-07-11 18:59:02
# Author: b4zinga
# Email : b4zinga@outlook.com
# Func  :

import base64
import requests

def run(url):
    weak = ['admin','s3cret','password','p@ssw0rd','1qaz2wsx', 'root', 'activemq', 'ActiveMQ']
    if ":8161" in url:
        url += '/admin/'
    else:
        url += ':8161/admin/'

    for user in weak:
        for pwd in weak:
            data = {'Authorization':'Basic '+base64.b64encode((user+':'+pwd).encode()).decode()}
            req = requests.get(url, headers=data, timeout=5)

            if not "Unauthorized" in req.text:
                msg = 'ActiveMQ weak password!\t'+ url+'\tusername:{}, pwd:{}'.format(user, pwd)
                return msg
    return False


