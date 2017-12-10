# -*- coding: utf-8 -*-
from django.shortcuts import render
from block.models import Block
from article.models import Article

def Detail(request,article_id):
    article_id=int(article_id)
    article=Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'art': article})