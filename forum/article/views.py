# -*- coding: utf-8 -*-
from django.shortcuts import render
from block.models import Block
from article.models import Article
from django.core.paginator import Paginator
def article_list(request,block_id):
    block_id = int(block_id)
    block=Block.objects.get(id=block_id)

    cut_page=4
    page_no = int(request.GET.get("page_no", "1"))
    all_article=Article.objects.filter(block=block,status=0).order_by("id")
    p=Paginator(all_article,cut_page)
    page=p.page(page_no)
    article_objs=page.object_list

    return render(request,'article_list.html',{'articles':article_objs,'b':block,
                                               'p':p,'page_no':page_no})

    # page_no=int(request.GET.get("page_no","1"))
    # start_page=(page_no-1)*cut_page
    # end_page=page_no*cut_page
    # [start_page:end_page]