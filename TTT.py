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


from pyecharts import Bar,Line

# attr=['收到资源','已打资源','未打资源','提交客户','成交客户']
# v1=[883,479,84,42,2]
# v2=[543,249,6,40,5]
# v3=[643,349,6,70,3]
# bar = Bar("标记线和标记点示例")
# bar.add("欧阳小蝶", attr, v1, mark_point=["max", "min"], is_stack=True)
# bar.add("申元吉", attr, v2, mark_line=["min", "max"], is_stack=True)
# bar.add("周凯", attr, v3, mark_line=["min", "max"], is_stack=True)
# bar.render()

attr=['收到资源','已打资源','未打资源','提交客户','成交客户']
v1=[883,479,84,42,2]
v2=[543,249,6,40,5]
v3=[643,349,6,70,3]
bar = Bar("标记线和标记点示例")
bar.add("欧阳小蝶", attr, v1, is_stack=True)
bar.add("申元吉", attr, v2,  is_stack=True)
bar.add("周凯", attr, v3, is_stack=True)
bar.render()

# line = Line("折线图示例")
# line.add("欧阳小蝶", attr, v1, is_smooth=True,mark_point=["max", "min"])
# line.add("申元吉", attr, v2 ,is_smooth=True, mark_line=["max", "min"])
# line.add("周凯", attr, v3 ,is_smooth=True, mark_line=["max", "min"])
# line.show_config()
# line.render()

# from pyecharts import Radar
# import numpy as np
# schema = [
#     ('收到资源', 1000), ('已打资源', 500), ('未打资源', 200), ('提交客户', 100), ('成交客户',10), ("质量过差数据", 500)]
#
# v1 = [[883, 479, 84, 42, 2, 404]]
#
# v2 = [348, 348, 0, 64, 2, 0]
#
# x=str([[{},{},{}]]).format(1,2,3)
# y=[1,2,3]
# # x.extend(y)
# print(list(x))
# exit()
# radar = Radar()
# radar.config(schema,rader_text_color="#000000",radar_text_size=14)
# radar.add("欧阳小蝶", v1, item_color="#CC0000",is_axisline_show=False)
# radar.add("申元吉", v2, item_color="#0044BB",is_axisline_show=False)
# radar.show_config()
# radar.render()



