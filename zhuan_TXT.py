# -*- coding: utf-8 -*-
# author:Super
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

# print df.columns[:-4]
# print df.columns[-4:]
# exit()

# for i in range(3):
#     for x in df.columns:
#         if x in df.columns[-4]:
#             val = df[x].loc[i].encode('gbk')
#             fl = open('%s.txt'%df['NAME'].loc[i], 'a')
#             if x=='NAME':
#                 fl.write('{\n')
#             else:
#                 fl.write('\t\r"{}\r"'.format(x) + ':' + '\r"' + str(val) +'\r"'+',')
#                 fl.write("\n")
#         else:


for i in range(3):
    for x in df.columns:
        val = df[x].loc[i]
        if x == 'number' or x == 'docUrl' or x == 'remark':
            val = val
        else:
            val = val.encode('gbk')

        fl = open('%s.txt' % df['name'].loc[i], 'a')
        if x == 'webName':
            fl.write('{\n')
            fl.write('\t\r"webUrl": "http://www.chictr.org.cn/searchproj.aspx"\n')
            fl.write('\t\r"{}\r"'.format(x.lower()) + ':' + '\r"' + str(val) + '\r"' + ',')
            fl.write("\n")
        elif x == 'remark':
            fl.write('\t\r"remark":"",\n')
        # elif x == 'docUrl':
        #     fl.write('\t\r"{}\r"'.format(x.lower()) + ':' + '\r"' + str(val) + '\r"' + ',')
        else:
            fl.write('\t\r"{}\r"'.format(x.lower()) + ':' + '\r"' + str(val) + '\r"' + ',')
            fl.write("\n")




