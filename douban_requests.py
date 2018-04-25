# -*- coding: utf-8 -*-

import requests
from lxml import etree

url='https://book.douban.com/subject/1084336/comments/'
r=requests.get(url).text

# print(r.status_code)
# print(r.apparent_encoding)

s=etree.HTML(r)

# #输出s对象
# print(s)

# #直接复制xpath路径
# print(s.xpath('/html/body/div[3]/div[1]/div/div[1]/div/div[2]/div/ul/li[1]/div[2]/p/text()')[0])

# #按标签优化提取
# print(s.xpath('//div[@class="comment"]/p/text()')[1])

# # 打印所有的评论
# list_comm=s.xpath('//div[@class="comment"]/p/text()')
# for comment in list_comm:
#     print(comment)


file = s.xpath('//div[@class="comment"]/p/text()')


import os
os.chdir('C:\Users\Administrator\Desktop')

# with open('comm.txt', 'w') as f:
#    for i in file:
#        i=i.encode('utf-8')
#        f.write(i)

import pandas as pd
df = pd.DataFrame(file)
df.to_excel('comm.xlsx',index=False)
