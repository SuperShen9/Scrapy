# -*- coding: utf-8 -*-
# author:Super
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
import codecs
import pandas as pd
import os,shutil
pd.set_option('expand_frame_repr',False)
os.chdir('C:\\Users\Administrator\Desktop')

df = pd.read_excel('sheet1.xlsx')
df_PC = pd.read_excel('sheet_PC.xlsx')
df_MV = pd.read_excel('sheet_MV.xlsx')

if os.path.exists('RUN'):
    shutil.rmtree('RUN')
os.makedirs('C:\\Users\Administrator\Desktop\\RUN')

os.chdir('C:\\Users\Administrator\Desktop\\RUN')

for i in range(df.shape[0]):
    fl = codecs.open('%s-%s-%s.txt' % (df['name'].loc[i], df['organization'].loc[i], df['webName'].loc[i]), 'a',"utf-8")
    for x in df.columns[:-2]:
        val = df[x].loc[i]
        if isinstance(val, float):
            val = ''
        else:
            val = val

        if x == 'webName':
            fl.write('\r{"webUrl": "",')
            fl.write('\r"{}": "{}",'.format(x, str(val).decode('utf-8')))

        else:
            fl.write('\r"{}": "{}",'.format(x, str(val).decode('utf-8')))
# 合并PC表
    uuid=df['uuid'].loc[i]
    fl.write('\r"PCinfo": [{')
    for ii in range(df_PC[df_PC['uuid']==uuid].shape[0]):
        for xx in df_PC.columns:
            val_pc = df_PC[xx].loc[ii]
            if  xx == 'time' :
                val_pc = val_pc
            else:
                val_pc = val_pc
            if xx=='uuid':
                pass
            elif xx=='WeChatSubName':
                fl.write('\r"{}": "{}"'.format(xx, str(val_pc).decode('utf-8')))

            else:
                fl.write('\r"{}": "{}",'.format(xx, str(val_pc).decode('utf-8')))
        if ii<df_PC[df_PC['uuid']==uuid].shape[0]-1:
            fl.write("}, {")
        else:
            pass
    fl.write("}],")

# 合并MV表
    fl.write('\r"MVinfo": [{')
    for iii in range(df_MV[df_MV['uuid']==uuid].shape[0]):
        for xxx in df_MV.columns:
            val_mv = df_MV[xxx].loc[iii]
            if xxx == 'time' or xxx=='isIndependentPub':
                val_mv = val_mv
            else:
                val_mv = val_mv
            if xxx == 'uuid':
                pass
            elif xxx=='isIndependentPub':
                fl.write('\r"{}": "{}"'.format(xxx, str(val_mv).decode('utf-8')))
            else:
                fl.write('\r"{}": "{}",'.format(xxx, str(val_mv).decode('utf-8')))

        if iii < df_MV[df_MV['uuid'] == uuid].shape[0] - 1:
            fl.write("}, {")
        else:
            pass
    fl.write("}],")

# 补充最后2个字段
    fl.write('\r"MDinfo": {')
    for x in df.columns[-2:]:
        val = df[x].loc[i]
        if isinstance(val, float):
            val = ''
        else:
            val = val
        if x=='WeChatSubName':
            fl.write('\r"{}": "{}"'.format(x, str(val).decode('utf-8')))
        else:
            fl.write('\r"{}": "{}",'.format(x, str(val).decode('utf-8')))
    fl.write("}}")






