# -*- coding: utf-8 -*-
# author:Super
import pandas as pd
import os,shutil
pd.set_option('expand_frame_repr',False)
os.chdir('C:\\Users\Administrator\Desktop')

df = pd.read_excel('sheet1.xlsx')
df_edu = pd.read_excel('sheet_edu.xlsx')
df_edu = df_edu.sort_values(by=['uuid','year','unitName'],ascending=[1,1,1])


if os.path.exists('RUN'):
    shutil.rmtree('RUN')
os.makedirs('C:\\Users\Administrator\Desktop\\RUN')

os.chdir('C:\\Users\Administrator\Desktop\\RUN')

for i in range(df.shape[0]):
    fl = open('%s-%s-%s.txt' % (df['name'].loc[i], df['organization'].loc[i], df['webName'].loc[i]), 'a')
    for x in df.columns:
        val = df[x].loc[i]
        if isinstance(val, float):
            val = ''
        else:
            val = val.encode('gbk')

        if x == 'webName':
            fl.write('{\n')
            fl.write('\t\r"webUrl": "http://xhgb.cma.org.cn/xuehui_project/listProjectGongbu.jsp?projectLevel=2&orgId=200100"\n')
            fl.write('\t\r"{}\r"'.format(x) + ':' + '\r"' + str(val) + '\r"' + ',')
            fl.write("\n")
        else:
            fl.write('\t\r"{}\r"'.format(x) + ':' + '\r"' + str(val) + '\r"' + ',')
            fl.write("\n")

    uuid=df['uuid'].loc[i]
    fl.write('\t\r"years": [{')

    # 遍历每一个人的信息
    for ii in range(df_edu[df_edu['uuid']==uuid].shape[0]):
        df_year=df_edu[df_edu['uuid']==uuid]
        df_year=df_year.reset_index(drop=True)
        # # print df_year
        #
        if ii < df_edu[df_edu['uuid']==uuid].shape[0]-1:
            year=df_year['year'].loc[ii]
            year1 = df_year['year'].loc[ii+1]
            cdt=year==year1
        #
        fl.write("\n")

        for xx in df_year.columns:
            val_edu = df_year[xx].loc[ii]
            if  xx == 'holdingPeriod' or xx == 'creditHour'or xx =='year':
                val_edu = val_edu
            else:
                val_edu = val_edu.encode('gbk')

            if xx=='uuid':
                pass
            elif xx=='year' :
                if not cdt:
                    fl.write('\t\t\r"{}\r"'.format(xx) + ':' + '\r"' + str(val_edu) + '\r"' + ',\n')
                    fl.write('\t\t\r"info": [{\n')
        #
            elif xx=='unitName' :
                fl.write('\t\t\t\r"{}\r"'.format(xx) + ':' + '\r"' + str(val_edu) + '\r"' + ',\n')
                fl.write('\t\t\t\r"unitInfo": [{\n')

            elif xx=='creditHour':
                fl.write('\t\t\t\t\t\r"{}\r"'.format(xx) + ':' + '\r"' + str(val_edu) + '\r"' + '\n')
            else:
                fl.write('\t\t\t\t\t\r"{}\r"'.format(xx) + ':' + '\r"' + str(val_edu) + '\r"' + ',\n')
        fl.write("\t\t\t\t}")










