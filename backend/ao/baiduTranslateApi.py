# -*- coding: utf-8 -*-
import requests
import json
import langid
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')

def ZH2FRA(context):
    url = 'http://fanyi.baidu.com/basetrans/'
    data = {
    'from':'zh',
    'to':'fra',
    'query':context,

    }
    headers ={"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}
    r = requests.post(url,data,headers=headers)
    r.encoding ="utf-8"

    dict_ret = json.loads(r.content.decode())
    ret = dict_ret["trans"][0]["dst"]
    return ret

def ZH2EN(context):
    url = 'http://fanyi.baidu.com/basetrans/'
    data = {
    'from':'zh',
    'to':'en',
    'query':context,

    }
    headers ={"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}
    r = requests.post(url,data,headers=headers)
    r.encoding ="utf-8"

    dict_ret = json.loads(r.content.decode())
    ret = dict_ret["trans"][0]["dst"]
    return ret

def EN2ZH(context):
    url = 'http://fanyi.baidu.com/basetrans/'
    data = {
    'from':'en',
    'to':'zh',
    'query':context,

    }
    headers ={"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}
    r = requests.post(url,data,headers=headers)
    r.encoding ="utf-8"

    dict_ret = json.loads(r.content.decode())
    ret = dict_ret["trans"][0]["dst"]
    return ret

def FR2ZH(context):
    url = 'http://fanyi.baidu.com/basetrans/'
    data = {
    'from':'fra',
    'to':'zh',
    'query':context,

    }
    headers ={"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}
    r = requests.post(url,data,headers=headers)
    r.encoding ="utf-8"

    dict_ret = json.loads(r.content.decode())
    ret = dict_ret["trans"][0]["dst"]
    return ret

def all2ZH(context):
    pattern = re.compile('[a-z，A-Z]+')
    match = pattern.findall(context)
    c = langid.classify(match[0])[0]
    if match.__len__() != 1 : return context,'unknown2zh'
    if c == 'en':
        ret = EN2ZH(match[0])
        if langid.classify(ret)[0] == 'zh':
            return ret,'en2zh'
        else:
            return context,'unknown2zh'
    elif c == 'fr':
        ret = FR2ZH(match[0])
        if langid.classify(ret)[0] == 'zh':
            return ret,'fr2zh'
        else:
            return context,'unknown2zh'
    else:
        return context,'unknown2zh'
