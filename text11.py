# -*- coding: utf-8 -*-
import os,xlrd
os.chdir('D:\zlianxi\hebing_excell')
# fath=unicode('E:\movie\美国众神','utf-8')
fath=unicode('D:\zlianxi\hebing_excell','utf-8')
for x,y,z, in os.walk(fath):

    for y1 in y:
        print type(y1)

    for z1 in z:
        wb = xlrd.open_workbook(z1)
        print type(z1)
        # print os.path.abspath('.\\'+y1)



