# -*- coding: utf-8 -*-
# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("Hello 驻足五秒")

from django.shortcuts import render
def index(request):
    block_infos=[{'name':'python','desc':'learning','owner':'super'},
                 {'name':'scrapy','desc':'learning','owner':'super'},
                 {'name':'django','desc':'learning','owner':'super'}]
    return render(request,"index.html",{'blocks':block_infos})

