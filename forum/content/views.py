# -*- coding: utf-8 -*-
from django.shortcuts import render
from block.models import Block
from content.models import Content
def content(request,block_id):
    block_id = int(block_id)
    block=Block.objects.get(id=block_id)
    content_objs=Content.objects.filter(block=block,status=0).order_by("id")
    return render(request,'content.html',{'contents':content_objs,'b':block})

