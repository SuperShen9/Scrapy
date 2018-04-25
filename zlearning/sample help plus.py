# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os,random
import pandas as pd
pd.set_option('expand_frame_repr',False)
os.chdir('C:\Users\Administrator\Desktop\Sample Data help')
df=pd.read_excel('text.xlsx')

df.fillna(method='ffill',inplace=True)

df_CN=df[df['country']=='CN']
df_CN.reset_index(drop=True,inplace=True)
df_EN=df[df['country']=='EN']
df_JA=df[df['country']=='JA']
df_KO=df[df['country']=='KO']
df_TW=df[df['country']=='TW']
# 重置index才能随机选取series

df_TW.reset_index(drop=True,inplace=True)
df_JA.reset_index(drop=True,inplace=True)
df_KO.reset_index(drop=True,inplace=True)

# print len(df_TW['First'])
# exit()

list_column=['First','last','job title','department','company name','address 1']


# 两项合并部分
def mix2(df1,df2):
    t1 = df1['country'][0]
    t2 = df2['country'][0]
    df_CN = df[df['country'] == 'CN']
    df_CN.reset_index(drop=True, inplace=True)
    df_CN = df[df['country'] == 'CN']
    df_CN.reset_index(drop=True, inplace=True)
    for i in range(df1.shape[0]):
        n = random.choice(list_column)
        df1[n].at[i] = random.choice(df2[n])
    df1.loc[:, 'Test Sample Type'] = '%s-%s' % (t1, t2)
    return df1


df_A=mix2(df_CN,df_EN)
# print df_A.head()


# 三项合并部分
def mix3(df1,df2,df3):
    t1=df1['country'][0]
    t2=df2['country'][0]
    t3=df3['country'][0]
    df_CN = df[df['country'] == 'CN']
    df_CN.reset_index(drop=True, inplace=True)
    for i in range(df1.shape[0]):
        n = random.choice(list_column)
        n1 = random.choice(list_column)
        df1[n1].at[i] = random.choice(df2[n1])
        df1[n].at[i] = random.choice(df3[n])
    df1.loc[:, 'Test Sample Type'] = '%s-%s-%s'%(t1,t2,t3)
    return df1

# df_B=mix3(df_CN,df_EN,df_TW)


print df_A.head(3)
# print df_B.head(3)

