# -*- coding: utf-8 -*-
from django.conf import settings
#初始化坏境
import os,sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AliCDN.settings")
import django
django.setup()

import urllib, urllib2
import base64
import hmac
import hashlib
from hashlib import sha1
import time
import uuid
import json
import traceback
import ConfigParser  #读取配置信息模块

# CONFIGFILE = os.getcwd() + '/aliyun.ini'

class Ali_Api(object):
    def __init__(self):
        # config = ConfigParser.ConfigParser()
        # config.read(CONFIGFILE)
        # self._access_key_id = config.get('Credentials', 'accesskeyid')
        # self._access_key_secret = config.get('Credentials', 'accesskeysecret')
        # self._cdn_server_address = config.get('Credentials', 'cdn_server_address')
        self._access_key_id = settings.ACCESSKEYID
        self._access_key_secret = settings.ACCESSKEYSECRET
        self._cdn_server_address = settings.CDN_SERVER_ADDRESS

        # Url编码
    def percent_encode(self,str):

        res = urllib.quote(str.decode('UTF-8').encode('utf8'), '')
        res = res.replace('+', '%20')
        res = res.replace('*', '%2A')
        res = res.replace('%7E', '~')
        return res

    def compute_signature(self,parameters, access_key_secret):
        sortedParameters = sorted(parameters.items(), key=lambda parameters: parameters[0])

        canonicalizedQueryString = ''
        for (k, v) in sortedParameters:
            canonicalizedQueryString += '&' + self.percent_encode(k) + '=' + self.percent_encode(v)

        stringToSign = 'GET&%2F&' + self.percent_encode(canonicalizedQueryString[1:])

        h = hmac.new(access_key_secret + "&", stringToSign, sha1)
        signature = base64.encodestring(h.digest()).strip()
        return signature

    def compose_url(self,user_params):
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

        parameters = { \
            'Format': 'JSON', \
            'Version': '2014-11-11', \
            'AccessKeyId': self._access_key_id  , \
            'SignatureVersion': '1.0', \
            'SignatureMethod': 'HMAC-SHA1', \
            'SignatureNonce': str(uuid.uuid1()), \
            'TimeStamp': timestamp, \
            }

        for key in user_params.keys():
            parameters[key] = user_params[key]
        signature = self.compute_signature(parameters, self._access_key_secret)
        parameters['Signature'] = signature
        url = self._cdn_server_address + "/?" + urllib.urlencode(parameters)
        return url

    def make_request(selt,user_params, quiet=False):
        url = selt.compose_url(user_params)
        result = urllib2.urlopen(url).read()
        return result

    def domains_info(self):
        All_info = {}
        DomainName = []
        user_params ={ 'Action': 'DescribeUserDomains', 'PageNumber': '1', 'PageSize':'5'}
        result=json.loads(self.make_request(dict(user_params)))
        for i in range(result["TotalCount"]):
            Domname=result["Domains"]["PageData"][i]["DomainName"]
            DomainName.append(Domname)
        All_info['TotalCount']=result['TotalCount']
        All_info['Domains']=DomainName
        return All_info

    def refresh_cashes(self,type,path):
        user_params = {'Action': 'RefreshObjectCaches', 'ObjectType': type, 'ObjectPath': path}
        try:
            result = self.make_request(dict(user_params))
            return result
        except Exception, e:
            return '请检查链接是否合法!'


#域名基本信息
# print  Ali_Api().domains_info()

#刷新缓存
# print Ali_Api().refresh_cashes(type='File',path='xxx.png')
#print json.loads(Ali_Api().make_request({'Action':'DescribeDomainBpsData'}))

#print Ali_Api().make_request({'Action':'DescribeDomainBpsData','TimeMerge':'20'})
#查询刷新操作记录
# print Ali_Api().make_request({'Action':'DescribeRefreshTasks','ObjectPath':'','PageNumber':'1','PageSize':'10'})

