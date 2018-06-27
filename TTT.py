# -*- coding: utf-8 -*-
# author:Super

# from Function import Sum_each
# import Function
#
# print Function.Sum_each('165646')

#递推法
# def climbStairs1(n):
#     a = 1
#     b = 2
#     c = 4
#     for i in range(n-3):
#         c, b, a = a+b+c, c, b
#     return c

#递归法
# def climbStairs2(n):
#     first3 = {1:1, 2:2, 3:4}
#     if n in first3.keys():
#         return first3[n]
#     else:
#         return climbStairs2(n-1) + climbStairs2(n-2) + climbStairs2(n-3)


# print(climbStairs1(4))
# print(climbStairs2(15))


import pandas as pd
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行

df=pd.read_excel('C:\\Users\Administrator\Desktop\电销-汇总.xlsx')

df.loc[7,'电销姓名']='电销汇总：'

for col in df.columns[2:]:
    df.loc[7,col]=df[col].sum()

df['提交率']=df['提交客户']/df['已打资源']
df['成交率']=df['成交客户']/df['已打资源']

print(df)

df.to_excel('C:\\Users\Administrator\Desktop\结果.xlsx',index=False)