# -*- coding: utf-8 -*-

import requests,time
import os
import pandas as pd

headers={
       'authorization': 'Bearer 2|1:0|10:1525075562|4:z_c0|92:Mi4xY0ZhY0F3QUFBQUFBTU9CNERYbUZEU1lBQUFCZ0FsVk5haHpVV3dBRHBCRXBMbk83OVo4TDk5VHVDTXpmalZBWE9n|65599041233aac4b4a7f994dc624cd1bb2461f47b78cf197aa0f7efec8eb7fe6'
        ,'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
}

follow_data=[]
def get_follow(page):
    for i in range(page):
        url = 'https://www.zhihu.com/api/v4/members/stormzhang/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_f' \
              'ollowed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20'.format(i*20)
        r=requests.get(url,headers=headers).json()['data']
        follow_data.extend(r)
        print('is crawling %s page'%str(i+1))
        time.sleep(2)

os.chdir('C:\Users\Administrator\Desktop')

get_follow(15)
df = pd.DataFrame.from_dict(follow_data)
df.to_excel('follow.xlsx',index=False)
