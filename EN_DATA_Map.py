# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os,openpyxl,xlrd
os.chdir('D:\zlianxi\EN_DATA_Map')
or_wb = openpyxl.load_workbook('data.xlsx')
sheet1 = or_wb.get_sheet_by_name('Sheet1')
sheet2 = or_wb.get_sheet_by_name('Sheet2')
wb = openpyxl.load_workbook('SAS_RE.xlsx')
ws = wb.get_sheet_by_name('data')
redict = {}
for row in range(2, ws.max_row + 1):
    word = ws['A' + str(row)].value
    replace = ws['B' + str(row)].value
    redict.setdefault(word, replace)
list1=[]
for row1 in range(2,sheet1.max_row+1):
    sheet1['D' + str(row1)]=sheet1['C' + str(row1)].value.lower().strip()
    list1.append(sheet1['D' + str(row1)].value)

#     for ky,ve in redict.items():
#         # sheet1['E' + str(row1)]=sheet1['D' + str(row1)].value.replace(str(ky),str(ve))
#         sheet1['E' + str(row1)]='jinhua shuhai zhiku m s b'.replace(str(ky),str(ve))
# # sheet1.freeze_panes='A2'
# # sheet2.freeze_panes='A2'
# sheet1['D1']='标准公司名称'
# sheet1['E1']='公司名简化'
# or_wb.save('data.xlsx')