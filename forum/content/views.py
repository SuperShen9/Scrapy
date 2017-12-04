# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from block.models import Block
from content.models import Content
from article.models import Article
def content(request,block_id):
    if request.method =='GET':
        block_id = int(block_id)
        block=Block.objects.get(id=block_id)
        content_objs=Content.objects.filter(block=block,status=0).order_by("id")
        return render(request,'content.html',{'contents':content_objs,'b':block})

    else:
        art_title =request.POST['art_title']
        art_content=request.POST['art_content']
        block_id = int(block_id)
        block = Block.objects.get(id=block_id)
        article = Article(block=block,title=art_title,content=art_content,status=0)
        article.save()
        return redirect('/article/list/%s'%block_id)

