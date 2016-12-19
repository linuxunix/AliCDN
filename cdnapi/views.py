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
    return  render(request, 'f5_cdn_file.html', locals())

@csrf_exempt
def get_file_result(request):
    if request.method == 'POST':
        file_path = request.POST.get('file_path')
        result = Ali_Api().refresh_cashes(type='file',path=file_path)
        return HttpResponse(json.dumps(result))

def f5_cdn_directory(request):
    result = Ali_Api().domains_info()
    return render(request, 'f5_cdn_directory.html', locals())

@csrf_exempt
def get_directory_result(request):
    if request.method == 'POST':
        file_path = request.POST.get('file_path')
        result = Ali_Api().refresh_cashes(type='Directory',path=file_path)
        return HttpResponse(json.dumps(result))

def f5_get_result(request):
    result = Ali_Api().domains_info()
    history_result = json.loads(Ali_Api().make_request({'Action':'DescribeRefreshTasks','ObjectPath':'','PageNumber':'1','PageSize':'15'}))
    history_result = history_result['Tasks']['CDNTask']
    return  render(request, 'f5_get_result.html', locals())