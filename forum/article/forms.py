# -*- coding: utf-8 -*-

from django import forms
class Articleform(forms.Form):
    art_title=forms.CharField(label="标题",max_length=100)
    art_content=forms.CharField(label="内容",max_length=10000)

