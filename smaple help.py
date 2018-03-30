# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os,random
import pandas as pd
pd.set_option('expand_frame_repr',False)
os.chdir('C:\Users\Administrator\Desktop\Sample Data help')
df=pd.read_excel('text.xlsx')

# df.fillna(method='ffill',inplace=True)


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

# print df.groupby('country').size()
# exit()

# print random.choice(df['First'])
# exit()

# df_CN.at[1389,'First']='hehe'
# print df_CN
# exit()

# 中英部分
for i in range(402):
    n = random.choice(list_column)
    df_CN[n].at[i]=random.choice(df_EN[n])
df_CN.loc[:,'Test Sample Type']='A'
df_A=df_CN

df_CN=df[df['country']=='CN']
df_CN.reset_index(drop=True,inplace=True)
# 中繁英部分
for i in range(410):
    n = random.choice(list_column)
    n1 = random.choice(list_column)
    df_CN[n1].at[i]=random.choice(df_EN[n1])
    df_CN[n].at[i]=random.choice(df_TW[n])

df_CN.loc[:,'Test Sample Type']='B'
df_A=df_A.append(df_CN)


df_CN=df[df['country']=='CN']
df_CN.reset_index(drop=True,inplace=True)
# 中繁部分
for i in range(410):
    n = random.choice(list_column)
    df_CN[n].at[i]=random.choice(df_TW[n])

df_CN.loc[:,'Test Sample Type']='C'
df_A=df_A.append(df_CN)

df_CN=df[df['country']=='CN']
df_CN.reset_index(drop=True,inplace=True)
# 中日部分
for i in range(402):
    n = random.choice(list_column)
    df_CN[n].at[i]=random.choice(df_JA[n])

df_CN.loc[:,'Test Sample Type']='F'
df_A=df_A.append(df_CN)


df_CN=df[df['country']=='CN']
df_CN.reset_index(drop=True,inplace=True)
# 中日英部分
for i in range(402):
    n = random.choice(list_column)
    n1 = random.choice(list_column)
    df_CN[n1].at[i] = random.choice(df_EN[n1])
    df_CN[n].at[i]=random.choice(df_JA[n])

df_CN.loc[:,'Test Sample Type']='G'
df_A=df_A.append(df_CN)


df_CN=df[df['country']=='CN']
df_CN.reset_index(drop=True,inplace=True)
# 中韩部分
for i in range(402):
    n = random.choice(list_column)
    df_CN[n].at[i]=random.choice(df_KO[n])

df_CN.loc[:,'Test Sample Type']='I'
df_A=df_A.append(df_CN)

df_CN=df[df['country']=='CN']
df_CN.reset_index(drop=True,inplace=True)
# 中韩英部分
for i in range(402):
    n = random.choice(list_column)
    n1 = random.choice(list_column)
    df_CN[n1].at[i] = random.choice(df_EN[n1])
    df_CN[n].at[i]=random.choice(df_KO[n])

df_CN.loc[:,'Test Sample Type']='H'
df_A=df_A.append(df_CN)

df_CN=df[df['country']=='CN']
df_CN.reset_index(drop=True,inplace=True)
df_CN.loc[:,'Test Sample Type']='D'
df_TW.loc[:,'Test Sample Type']='E'
df_A=df_A.append(df_CN).append(df_TW)


print df_A.groupby('Test Sample Type').size()

# os.chdir('C:\Users\Administrator\Desktop')
# df_CN.to_excel('CN.xlsx',index=False)





# list_china=[]
# for i in df_china['job title']:
#     list_china.append(i)
#
# list_english=[]
# for i in df_english['job title']:
#     list_english.append(i)
# df_out=pd.DataFrame()
# for j in range(20):
#     df_out.at[j,'last']=random.choice(list_china)+random.choice(list_english)
# print df_out


# df_out=pd.DataFrame()
# for n in list(df):
#     list_china=[]
#     for i in df_china[n]:
#         list_china.append(i)
#
#     list_english=[]
#     for i in df_english[n]:
#         list_english.append(i)
#
#     for j in range(20):
#         df_out.at[j,n]=str(random.choice(list_china))+str(random.choice(list_english))
# print df_out