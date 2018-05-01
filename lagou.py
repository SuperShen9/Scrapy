# -*- coding: utf-8 -*-

from pymongo import MongoClient
client = MongoClient()
db = client.lagou
lagou_job = db.set

import requests,time
import os
import pandas as pd

from fake_useragent import UserAgent

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
headers = {
            'Cookie':'JSESSIONID=ABAAABAAADEAAFI117FBDB5C77AB77BD9B807D2C7D68148; _ga=GA1.2.555489736.1525146654; _gid=GA1.2.1910315277.1525146654; index_location_city=%E5%85%A8%E5%9B%BD; user_trace_token=20180501115110-e2b661f7-4cf2-11e8-a93f-525400f775ce; LGSID=20180501115110-e2b66379-4cf2-11e8-a93f-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20180501115110-e2b665de-4cf2-11e8-a93f-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1525146670; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1525147994; LGRID=20180501121316-f952402f-4cf5-11e8-bb05-5254005c3644; TG-TRACK-CODE=search_code; SEARCH_ID=7fbc97da6259499783e9e3f4904dcd48',
            'Referer':'https://www.lagou.com/jobs/list_%E5%8C%BA%E5%9D%97%E9%93%BE?labelWords=&fromSearch=true&suginput=',
        }

def get_job(page,kd):
    for i in range(page):
        payload = {
            'first':'true',
            'pn':i,
            'kd':kd,
        }
        ua=UserAgent()
        headers['User-Agent'] = ua.random
        response = requests.post(url, data = payload, headers = headers)

        if response.status_code == 200:
            job = response.json()['content']['positionResult']['result']
            lagou_job.insert(job)
        else:
            print('Something Wrong!')

        print('正在爬取' + str(i + 1) + '页的数据...')
        time.sleep(3)

get_job(30, '区块链')

# os.chdir('C:\Users\Administrator\Desktop')
# df = pd.DataFrame(job)
# df.to_excel('lagou_job.xlsx',index=False)



