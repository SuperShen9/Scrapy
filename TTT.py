# -*- coding: utf-8 -*-
# author:Super
import re
a='86-3254888753/456'
# b=None
# a=str(b)
num_Regex=re.compile(r'\d+')
num_Regex1=re.compile(r'^886-|^86-')
gz_Regex=re.compile(r'^02')
mo=num_Regex.findall(a)
mo1=num_Regex1.sub('0',a)
mo2=num_Regex.findall(mo1)
mo3='-'.join(mo2)
mo4=gz_Regex.sub('02-',mo3)
print 'mo:' + str(mo)
print 'mo1:'+ str(mo1)
print 'mo2'+ str(mo2)
print '-'.join(mo2)
print mo4