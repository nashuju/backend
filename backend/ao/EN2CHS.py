# -*- coding: utf-8 -*-

import httplib
import md5
import urllib
import random
import json
class EN2CHS:

    translation = ''
    basic = ''
    result = {}

    def __init__(self,EN):
        appKey = '7be6e3a51ab94c85'
        secretKey = 'XgvfRxF0jVdf5weaulpScqzScqae0936'
        httpClient = None
        myurl = '/api'
        fromLang = 'EN'
        toLang = 'zh-CHS'
        salt = random.randint(1, 65536)
        sign = appKey+EN+str(salt)+secretKey
        m1 = md5.new()
        m1.update(sign)
        sign = m1.hexdigest()
        myurl = myurl+'?appKey='+appKey+'&q='+urllib.quote(EN)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign

        try:
            httpClient = httplib.HTTPConnection('openapi.youdao.com')
            httpClient.request('GET', myurl)
            #response是HTTPResponse对象
            response = httpClient.getresponse()
            self.result = json.loads(response.read())
            self.translation = self.result['translation'][0]
            self.basic = self.basic.join(self.result['basic']['explains'])
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()

#t = EN2CHS('One problem is that RNNs are not inductive')

pass