# -*- coding: utf-8 -*-
import random
import pprint
dict={}
list1 = ['+', '-']
while True:
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    c=random.choice(list1)
    if (c=='-' and a>b) or (c=='+' and a+b<100):
        astr=str(a)+c+str(b)
        bstr=str(b)+c+str(a)
        if dict.get(bstr,0)==0:
            dict.setdefault(astr,'aaa')
            if len(dict)==36:
                break
count1=1
print '题目：'
for ky in dict.keys():
    if count1==4:
        print str(ky[:2])+ str(ky[2]) + str(ky[3:])+ ' ='+' '*10
        count1=1
    else:
        print str(ky[:2]) + str(ky[2]) + str(ky[3:]) + ' ='+' '*10,
        count1+=1
print '\n'
print '答案：'
print '-' *100
count2=1
for ky in dict.keys():
    if count2==4:
        if ky[2]=='+':
            print str(int(ky[:2]) + int(ky[3:])).ljust(18)

        else:
            print str(int(ky[:2]) - int(ky[3:])).ljust(18)
        count2=1
    else:
        if ky[2] == '+':
            print str(int(ky[:2]) + int(ky[3:])).ljust(18),

        else:
            print str(int(ky[:2]) - int(ky[3:])).ljust(18),
        count2+=1

