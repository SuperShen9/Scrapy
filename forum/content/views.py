# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from block.models import Block
from article.models import Article

def content(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)

    if request.method =='GET':
        return render(request,'content.html',{'b':block})

    else:
        art_title =request.POST['art_title'].strip()
        art_content=request.POST['art_content'].strip()

        if not art_title or not art_content:
            return render(request,'content.html',
                          {'b': block,"error":"标题和内容不能为空",
                           'art_title':art_title,'art_content':art_content})

        if len(art_title)>100 or len(art_content)>10000:
            return render(request, 'content.html',
                          {'b': block, "error": "标题和内容太长",
                           'art_title': art_title, 'art_content': art_content})

        article = Article(block=block,title=art_title,content=art_content,status=0)
        article.save()
        return redirect('/article/list/%s'%block_id)

