# -*- coding: utf-8 -*-
# author:Super
import pandas as pd
import os,shutil
pd.set_option('expand_frame_repr',False)
os.chdir('C:\\Users\Administrator\Desktop')

df = pd.read_excel('sheet1.xlsx')
df_PC = pd.read_excel('sheet_PC.xlsx')
df_MV = pd.read_excel('sheet_MV.xlsx')

# df=pd.merge(left=df, right=df_PC, on=['uuid'],how='right')
# df=pd.merge(left=df, right=df_MV, on=['uuid'],how='right')
# print df.info()
# os.chdir('C:\\Users\Administrator\Desktop')
# df.to_excel('1.xlsx')
# exit()

if os.path.exists('RUN'):
    shutil.rmtree('RUN')
os.makedirs('C:\\Users\Administrator\Desktop\\RUN')

os.chdir('C:\\Users\Administrator\Desktop\\RUN')



# for i in range(df.shape[0]):
#     count=0
#     for x in df.columns:
#         count+=1
#         val = df[x].loc[i]
#         # if x == 'docUrl' or x == 'remark':
#         #     val = val
#         if isinstance(val, float):
#             val = ''
#         else:
#             val = val.encode('gbk')
#         fl = open('%s-%s-%s.txt' % (df['name'].loc[i],df['organization'].loc[i],df['webName'].loc[i]), 'a')
#         if count<=len(df.columns)-4:
#             if x == 'webName':
#                 fl.write('{\n')
#                 fl.write('\t\r"webUrl": "http://www.chictr.org.cn/searchproj.aspx"\n')
#                 fl.write('\t\r"{}\r"'.format(x) + ':' + '\r"' + str(val) + '\r"' + ',')
#                 fl.write("\n")
#             elif x == 'remark':
#                 fl.write('\t\r"remark":"",\n')
#             else:
#                 fl.write('\t\r"{}\r"'.format(x) + ':' + '\r"' + str(val) + '\r"' + ',')
#                 fl.write("\n")
#         elif count==len(df.columns)-3:
#             fl.write('\t\r"info": {\n')
#             fl.write('\t\t\r"name\r"' + ':' + '\r"' + str(val) + '\r"' + ',\n')
#
#         elif count==len(df.columns)-1:
#             if val[-1]=='0':
#                 fl.write('\t\t\r"{}\r"'.format(x) + ':' + '\r"' + str(val)[:4] + '\r"' + ',\n')
#             else:
#                 fl.write('\t\t\r"{}\r"'.format(x) + ':' + '\r"' + str(val)[4:] + '\r"' + ',\n')
#
#         elif count == len(df.columns) :
#             fl.write('\t\t\r"{}\r"'.format(x) + ':' + '\r"' + str(val) + '\r"' + ',\n')
#             fl.write('\t}\n')
#             fl.write('}')
#         else:
#             fl.write('\t\t\r"{}\r"'.format(x) + ':' + '\r"' + str(val) + '\r"' + ',')
#             fl.write("\n")




