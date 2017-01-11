# -*- coding:utf8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import ConfigParser  #读取配置信息模块
from django.views.decorators.csrf import csrf_exempt
from Ali_Cdn_Api import *
import json
# Create your views here.

def f5_cdn_file(request):
    result = Ali_Api().domains_info()
    DescribeRefreshQuota = json.loads(Ali_Api().make_request({'Action':'DescribeRefreshQuota'}))
    UrlRemain=DescribeRefreshQuota["UrlRemain"]
    DirRemain = DescribeRefreshQuota["DirRemain"]
    return  render(request, 'f5_cdn_file.html', locals())

@csrf_exempt
def get_file_result(request):
    if request.method == 'POST':
        file_path = request.POST.get('file_path')
        result = Ali_Api().refresh_cashes(type='file',path=file_path)
        return HttpResponse(json.dumps(result))



def f5_cdn_directory(request):
    result = Ali_Api().domains_info()
    DescribeRefreshQuota = json.loads(Ali_Api().make_request({'Action':'DescribeRefreshQuota'}))
    DirRemain = DescribeRefreshQuota["DirRemain"]
    return render(request, 'f5_cdn_directory.html', locals())

@csrf_exempt
def get_directory_result(request):
    if request.method == 'POST':
        file_path = request.POST.get('file_path')
        result = Ali_Api().refresh_cashes(type='Directory',path=file_path)
        return HttpResponse(json.dumps(result))

@csrf_exempt
def f5_get_result(request):
    result = Ali_Api().domains_info()
    if request.method == 'POST':
        history_result = json.loads(Ali_Api().make_request({'Action':'DescribeRefreshTasks','ObjectPath':'','PageNumber':'1','PageSize':'15'}))
        return HttpResponse(json.dumps(history_result))
    # history_result = history_result['Tasks']['CDNTask']
    return  render(request, 'f5_get_result.html', locals())


def DescribeDomainFlowData(request):
    result = json.loads(Ali_Api().make_request({'Action': 'DescribeDomainFlowData'}))
    return HttpResponse(json.dumps(result))

def DescribeDomainsUsageByDay(request):
    result = json.loads(Ali_Api().make_request({'Action': 'DescribeDomainsUsageByDay'}))
    return HttpResponse(json.dumps(result))

def UsageByDay(request):
    return render(request, 'detailed/UsageByDay.html', locals())