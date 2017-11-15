# -*- coding: utf-8 -*-
# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("Hello 驻足五秒")

from django.shortcuts import render
def index(request):
    return render(request,"index.html")

