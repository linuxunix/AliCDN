"""AliCDN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from cdnapi import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.f5_cdn_file,name='f5_cdn_file'),
    url(r'^get_file_result/', views.get_file_result, name='get_file_result'),
    url(r'^f5_cdn_directory/',views.f5_cdn_directory,name='f5_cdn_directory'),
    url(r'^get_directory_result/', views.get_directory_result, name='get_directory_result'),
    url(r'^f5_get_result/', views.f5_get_result, name='f5_get_result'),
    url(r'^DescribeDomainFlowData/', views.DescribeDomainFlowData, name='DescribeDomainFlowData'),
    url(r'^detailed/DescribeDomainsUsageByDay/', views.DescribeDomainsUsageByDay, name='DescribeDomainsUsageByDay'),
    url(r'^detailed/UsageByDay/', views.UsageByDay, name='UsageByDay'),
    url(r'^detailed/UsageByDay', TemplateView.as_view(template_name="detailed/UsageByDay.html"), name='UsageByDay'),
    url(r'^demo/',TemplateView.as_view(template_name="demo.html"))
]
