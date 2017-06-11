# -*- coding: utf-8 -*-
import os,xlrd
os.chdir('D:\zlianxi\hebing_excell')
# fath=unicode('E:\movie\美国众神','utf-8')
fath=unicode('D:\zlianxi\hebing_excell','utf-8')
fath1=unicode('D:\zlianxi\hebing_excell1','utf-8')
for x,y,z, in os.walk(fath):
    # print x
    # print '-' * 50
    # for y1 in y:
    #     print y1
    #     print '+'*20
    for z1 in z:
        print z1
        print type(z1)
print '-'*50
for x1, y1, zz, in os.walk(fath):
    for z1 in zz:
        print z1
        print type(z1)



        # print os.path.abspath('.\\'+y1)



