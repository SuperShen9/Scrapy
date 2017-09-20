# -*- coding: utf-8 -*-
import random
# count=1
# for i in range(36):
#     a = random.randint(1, 9)
#     b = random.randint(1, 9)
#     if count==4:
#         print str(a)+' x '+str(b)+' =   '
#         count=1
#     else:
#         print str(a) + ' x ' + str(b)+' =   ',
#         count += 1
import pprint
dict={}
while True:
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    astr=str(a)+str(b)
    bstr=astr[::-1]
    if dict.get(bstr,0)==0:
        dict.setdefault(astr,'aaa')
        if len(dict)==36:
            break
count1=1
for ky in dict.keys():
    if count1==4:
        print str(ky[0])+' x '+str(ky[1])+ ' =   '
        count1=1
    else:
        print str(ky[0]) + ' x ' + str(ky[1]) + ' =   ',
        count1+=1
print '----------------------------------------'
count2=1
for ky in dict.keys():
    if count2==4:
        print str(int(ky[0])*int(ky[1])).ljust(10)
        count2=1
    else:
        print str(int(ky[0])*int(ky[1])).ljust(10),
        count2+=1

