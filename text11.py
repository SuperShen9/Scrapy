# -*- coding: utf-8 -*-
# author:Super
# from random import sample,randint
# def ab(a,b):
#     return sum(1 for ch in a if ch not in b)
#
# def tp(a,b,position):
#     pa=[a[p] for p in position]
#     print pa
#     # 获取a中指定位置的字母
#     pb=[b[p:].index(ch)+p for p,ch in zip(position,pa) if ch in b[p:]]
#     print pb
#     if sorted(pb)==pb:
#         return True
#     return False
# def main(a,b,rateNumber=1.0):
#     c1=ab(a,b)
#     c2=ab(b,a)
#     r=abs(c1-c2)/len(a+b)
#     minlength=min(len(a),len(b))
#     positon=sample(range(minlength),randint(minlength//2,minlength-1))
#     positon.sort()
#     flag=tp(a,b,positon)
#     if flag and r<rateNumber:
#         return True
#     return False
#
# print main('python','pyethon',rateNumber=0.2)

for i in range(1,2):
    print i