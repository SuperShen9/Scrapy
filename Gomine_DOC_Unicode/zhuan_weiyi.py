# -*- coding: utf-8 -*-
# author:Super
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import codecs
import pandas as pd
import time,os,shutil

pd.set_option('expand_frame_repr',False)
os.chdir('C:\\Users\Administrator\Desktop')
# #openpyxl模块
# wb = openpyxl.load_workbook('sheet1.xlsx')
# sheet = wb.get_sheet_by_name('Sheet1')
# print sheet['A2'].value
# print type(sheet['A2'].value.encode("gbk"))
# exit()

# # 查看text文件
# file=open('text.txt')
# lines=file.readlines()
# print lines
# for i in lines:
#     print i
# exit()

df=pd.read_excel('sheet1.xlsx')

if os.path.exists('RUN'):
    shutil.rmtree('RUN')
os.makedirs('C:\\Users\Administrator\Desktop\\RUN')
os.chdir('C:\\Users\Administrator\Desktop\\RUN')
# df.shape[0]

for i in range(df.shape[0]):
    count=0
    for x in df.columns:
        count+=1
        val = df[x].loc[i]

        if isinstance(val, float):
            val = ''
        else:
            val = val

        fl = codecs.open('%s-%s-%s.txt' % (df['name'].loc[i],df['organization'].loc[i],df['webName'].loc[i]), 'a',"utf-8")
        if count<=len(df.columns)-4:
            if x == 'webName':
                fl.write('\r{"webUrl": "http://www.chictr.org.cn/searchproj.aspx",')
                fl.write('\r"{}": "{}",'.format(x, str(val).decode('utf-8')))
            elif x == 'remark':
                fl.write('\r"remark":"",')
            else:
                fl.write('\r"{}": "{}",'.format(x, str(val).decode('utf-8')))

        elif count==len(df.columns)-3:
            fl.write('\r"info": {')
            fl.write('\r"name": "{}",'.format(str(val).decode('utf-8')))

        elif count==len(df.columns)-1:
            if val==0:
                fl.write('\r"{}": "{}",'.format(x, u'暂无'))
            else:
                fl.write('\r"{}": "{}",'.format(x, str(val).decode('utf-8')))

        elif count == len(df.columns):
            fl.write('\r"{}": "{}"'.format(x, str(val).decode('utf-8')))
            fl.write('}')
            fl.write('}')
        else:
            fl.write('\r"{}": "{}",'.format(x, str(val).decode('utf-8')))





