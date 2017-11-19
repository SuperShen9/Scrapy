# -*- coding: utf-8 -*-
from django.db import models

class Block(models.Model):
    name = models.CharField(u'板块名称',max_length=100)
    owner = models.CharField(u'管理员', max_length=100)
    desc = models.CharField(u'板块信息', max_length=100)

