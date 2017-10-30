# -*- coding: utf-8 -*-
from __future__ import division
def ab(a,b):
    return sum(1 for ch in a if ch not in b)
def sim(a,b):
    c1 = ab(a, b)
    c2 = ab(b, a)
    s=1-(c1+c2)/len(a+b)
    print ('%.f%%' % (s * 100))

sim('abc','bca')
