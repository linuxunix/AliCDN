# -*- coding: UTF-8 -*-
from django.test import TestCase

# Create your tests here.
#!/usr/bin/env python

# FileName: login
import time
import urllib
import urllib2
import cookielib
import sys

login_url='http://192.168.10.122/j_acegi_security_check'

def login(username,password):
    username = username
    password = password
    #remember_me = 'false'
    #from = '/'
    #crumb = ''
    #password = hashlib.md5(password_src).hexdigest()
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent','Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.1)')]
    urllib2.install_opener(opener)
    #req = urllib2.Request(login_url,urllib.urlencode({"j_username":username,"j_password":password,"remember_me": 'false', "from": "/", "crumb": "a502af09b3999031307e333bab7c0a8a"}))
    req = urllib2.Request(login_url,urllib.urlencode({"j_username":username,"j_password":password,"remember_me": 'false', "from": "/", "crumb": "a502af09b3999031307e333bab7c0a8a"}))
    #req.add_header("Referer","")
    resp = urllib2.urlopen(req)
    #print resp.read()
    return cj

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print u'请输入选项参数： -URL -username -password -filename\n'
        sys.exit(0)
    url = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    filename = sys.argv[4]
    #print "%s\n%s\n %s" % (url,username,password)
    cj = login(username,password)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent','Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.1)')]
    urllib2.install_opener(opener)
    re = urllib2.Request(url)
    rs = urllib2.urlopen(re).read()
    #print filename
    open(filename,'w').write(rs)

